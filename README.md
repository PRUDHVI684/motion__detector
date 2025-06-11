# motion__detector
**Motion Detector using OpenCV**
This project is a simple Motion Detector built with Python and OpenCV. It captures real-time video from a webcam and detects any movement by comparing frames. When motion is detected, it can optionally save a frame/image for further review.

**features**
Real-time motion detection using webcam

Frame differencing with thresholding

Visual feedback with bounding boxes on moving objects

Optional image capture upon motion detection

Lightweight and easy to set up

**requriments**

Python 3.x (preferably 3.8 - 3.10)
OpenCV (opencv-python)

 **How It Works**
 
The webcam continuously captures video frames.

The script compares the current frame with the previous one.

If a significant difference is detected (motion), it highlights the motion region.

Optionally, the frame is saved as an image for later review.

**Output**

Motion regions highlighted in the webcam feed

**Use cases**

Basic home security system

Monitor pet or room activity

Motion-triggered photo capture

