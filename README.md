# ROS 2 Real-Time Face Tracker

A lightweight, real-time computer vision node for ROS 2 Humble that utilizes OpenCV's Haar Cascades to detect and track human faces via a standard USB webcam stream. 

This package is optimized for real-time robotic applications, featuring a zero-lag message queue and dynamic lighting adjustments using CLAHE (Contrast Limited Adaptive Histogram Equalization).

## Features
* **Real-Time Processing:** Optimized QoS settings (queue size of 1) ensure the node only processes the most recent frame, eliminating lag build-up in the CV pipeline.
* **Dynamic Contrast Adjustment:** Integrates OpenCV CLAHE to automatically balance lighting and contrast, allowing for accurate Haar Cascade detection even in dim or backlit environments.
* **Self-Contained Launch System:** Includes a custom `launch` file to spin up both the hardware camera drivers and the vision processing node simultaneously.

## Prerequisites
* **OS:** Ubuntu 22.04 (Jammy Jellyfish)
* **ROS Version:** ROS 2 Humble Hawksbill
* **Hardware:** Any standard UVC-compatible USB or integrated laptop camera.

## Installation

### 1. System Dependencies
Ensure you have the required ROS 2 packages and Python libraries installed. 

*Note: This package requires `numpy<2` to maintain compatibility with the ROS 2 Humble `cv_bridge` binaries.*

```bash
sudo apt update
sudo apt install ros-humble-usb-cam ros-humble-cv-bridge python3-opencv
pip3 install "numpy<2"

2. Workspace Setup

Clone this repository into the src directory of your ROS 2 workspace.
Bash

mkdir -p ~/vision_ws/src
cd ~/vision_ws/src
git clone [https://github.com/abinaabey2006/face_tracker.git](https://github.com/abinaabey2006/face_tracker.git)

3. Build the Package

Return to the root of your workspace and compile the package using colcon.
Bash

cd ~/vision_ws
colcon build --packages-select face_tracker

Usage
Launching the Tracker

Source your workspace and use the provided launch file. This will automatically start the camera feed and the tracking node.
Bash

source ~/vision_ws/install/setup.bash
ros2 launch face_tracker tracker.launch.py

Viewing the Output

To view the live video stream with the generated bounding boxes, open a new terminal and launch rqt_image_view.
Bash

source /opt/ros/humble/setup.bash
ros2 run rqt_image_view rqt_image_view

    Select the /face_tracking/output topic from the dropdown menu in the top left corner of the GUI.
