# VisionWasteClassifier
VisionWasteClassifier: Real-Time Waste Classification System

A real-time waste classification system developed using computer vision and deep learning. This project utilizes OpenCV and cvzone libraries to process live video streams and overlay waste classification results on the screen. The system is capable of identifying and categorizing various waste items images through a webcam feed.

**Features**
- Real-Time Classification: The system captures video from the webcam and processes it in real time, providing instant waste classification results.

- Overlay Visualization: Waste classification results are visually overlaid on the video feed. The system dynamically displays the waste item's category on the screen.

- Disposal Instructions: The system enhances user awareness by overlaying appropriate disposal instructions and bin indicators on the video feed.

**Requirements**
- Python 3.x
- OpenCV (cv2)
- cvzone (ClassificationModule)

**Installation**
- Clone or download this repository to your local machine.
- Install the required libraries by running: pip install opencv-python cvzone

**Usage**
- Run the main.py script.
- The application will start using your webcam to capture video.
- Hold waste items in front of the camera, and the system will classify them in real time.
- The waste item's category will be overlaid on the video feed.
- Dispose of the waste item according to the provided disposal instructions.

**Folder Structure**
- main.py: The main Python script for the real-time waste classification system.
- Resources/
  - Model/: Folder containing the trained deep learning model and labels.
  - Waste/: Folder containing images of different waste items for classification.
  - Bins/: Folder containing images of waste bins corresponding to different waste categories.

**Customization**

To improve waste classification accuracy, you can train your own deep learning model using your dataset.
Modify the disposal instructions and bin indicators in the Resources/ folder to match your specific needs.

**Credits**

This project uses the cvzone library's ClassificationModule for classification. Credit goes to cvzone for their contribution to computer vision.

**Note**

The initial project idea is inspired by cvzone. While the project concept is based on cvzone, the code has been modified and tailored to meet specific project requirements and enhancements.





