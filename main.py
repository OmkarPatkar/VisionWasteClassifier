import os
import cvzone
from cvzone.ClassificationModule import Classifier
import cv2

# Function to load images from a directory
def load_images(directory):
    # Load images from a directory and return them as a list.
    image_list = []
    path_list = os.listdir(directory)
    for path in path_list:
        image_list.append(cv2.imread(os.path.join(directory, path), cv2.IMREAD_UNCHANGED))
    return image_list

# Function to overlay images
def overlay_image(background, overlay, position):
    # Overlay an image on the background at the specified position.
    return cvzone.overlayPNG(background, overlay, position)

# Function to get the corresponding bin class based on the classification
def get_bin_class(class_id):
    # Map the classification class to the corresponding bin class.
    class_dict = {
        0: None,
        1: 0,
        2: 0,
        3: 3,
        4: 3,
        5: 1,
        6: 1,
        7: 2,
        8: 2
    }
    return class_dict.get(class_id, None)

def main():
    # Initialize video capture and the classifier
    cap = cv2.VideoCapture(0)
    classifier = Classifier('Resources/Model/keras_model.h5', 'Resources/Model/labels.txt')
    img_arrow = cv2.imread('Resources/arrow.png', cv2.IMREAD_UNCHANGED)

    image_list = load_images('Resources/Waste')
    bins_list = load_images('Resources/Bins')

    while True:
        # Read the frame from the camera
        _, frame = cap.read()
        img_resize = cv2.resize(frame, (529, 297))
        img_background = cv2.imread('Resources/background.png')

        # Get the prediction from the classifier
        prediction = classifier.getPrediction(frame)
        class_id = prediction[1]

        if class_id != 0:
            # Overlay the waste image and arrow on the background
            img_background = overlay_image(img_background, image_list[class_id - 1], (909, 127))
            img_background = overlay_image(img_background, img_arrow, (978, 320))
            bin_class_id = get_bin_class(class_id)
        else:
            bin_class_id = 0

        # Overlay the corresponding bin image on the background
        img_background = overlay_image(img_background, bins_list[bin_class_id], (895, 374))
        img_background[170:170 + 297, 121:121 + 529] = img_resize

        # Display the modified background
        cv2.imshow("Waste Classifier", img_background)

        # Press 'Esc' to exit the loop
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Release the video capture when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
