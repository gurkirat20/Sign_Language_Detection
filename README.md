# Sign Language Detection

<p>This is a Sign language detection model that can accurately recognize and interpret the gestures and movements of hands used in **American Sign Language (ASL)**.</p>
<p>
The model processes real-time video data and provide real-time feedback on the signs being performed. The end goal of this project is to create a tool that can help bridge communication gaps between deaf and hearing individuals, and enable more inclusive and accessible interactions in various settings.
</p>

![American Sign Language](sign-language-alphabet.png)
<p>The image shows signs of the alphabets in ASL.</p>


## Get Started

<p>You can run this model on your system by installing a couple of things --
- [Python](https://www.python.org/downloads/)
- [Mediapipe](https://developers.google.com/mediapipe/framework/getting_started/install)
- Python libraries and modules like OpenCV, Time and OS
You can get started by checking out any of the setup guides for their installation. However, links of official sites and guides have been attached. </p>


## Framework:

### Mediapipe : 

<p>MediaPipe is an open-source framework developed by Google that provides a set of pre-built, customizable building blocks for building multimodal machine learning pipelines. MediaPipe is built on top of TensorFlow, a popular open-source machine learning framework. </p>

<p> MediaPipe can be used to develop applications for a wide range of multimedia processing tasks, including audio and video processing, gesture recognition, object detection, and augmented reality. In this project, we used the pre-built hand tracking model of medipipe to develop our system. </p>

<p>For more about Mediapipe, you can visit the official site of [Mediapipe](https://developers.google.com/mediapipe) or [linked Github repository](https://github.com/google/mediapipe).

----

## Working of the project:

### 1.Input data:

<p>The module takes in video or image data as input, which contains one or more hands to
be tracked. </p>

### 2.Pre-processing:

<p>The input data is pre-processed to prepare it for analysis. This may involve resizing,
normalization, or any other required data transformations. </p>

### 3.Architecture

<p>The hand landmarker model bundle contains a palm detection model and a hand landmarks detection model. </p>

### 4.Hand detection: 

<p>The first step in hand tracking is to detect the presence of a hand in the input data. The imported module (mediapipe) uses a machine learning model to detect the hand in each frame of the video or image. The Palm detection model locates hands within the input image, and the hand landmarks detection model identifies specific hand landmarks on the cropped hand image defined by the palm detection model. </p>

### 5.Hand landmark estimation: 

<p>Once a hand has been detected, the MediaPipe Hand Tracking module uses another machine learning model to estimate the positions of 21 landmarks on the hand, such as the fingertips, knuckles, and wrist. </p>

### 6.Hand tracking:

<p>The estimated hand landmarks are then tracked across frames of the video or image data to determine the hand's movements and gestures. </p>

### 7.Post-processing: 

<p>Once the hand has been tracked, the output data is post-processed to make it easier to understand or use. In our code we have returned a list of tuples of id no. , x ,y and z coordinated of each of the 21 landmarks for further use in sign detection.

### 8.Output visualization: 

<p>Finally, the results of the hand tracking analysis are visualized as text on the user’s screen. </p>

## System Requirements

-The operating system should be compatible with the MediaPipe framework and
any additional software or libraries used in the application.
-The processor should have sufficient processing power to handle real-time video
data and machine learning computations.
-A camera with at least 720p resolution and 30 frames per second (fps) is
recommended for capturing video data.

However, the model uses Mediapipe framework which is a lighweight framework and can be used for mobile ml solutions.

## Contributars

- [Gurkirat Singh](https://github.com/gurkirat20)
- Astha Singh
