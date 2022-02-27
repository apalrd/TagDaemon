## Tag Daemon

This project monitors camera streams for fiducial markers (using the AprilTags library), and publishes resulting data to MQTT for use by other programs. In addition, JPEG images are published as they are processed.

### Current Status
The project is currently in development.

The following features are currently believed to work:
* RTSP based camera stream input and decoding using a single class of AprilTag for multiple cameras
* MQTT publishing of detections per camera

The following features are planned:
* MQTT publishing of the largest tag in addition to the substructure for each tag
* MQTT publishing of the JPEG image used for analysis
* Companion python program to view streams over MQTT and add overlays (similar to AprilTag examples)
* Passthrough of hardare acceleration arguments to ffmpeg (used by OpenCV) for video decoding
* Support for JPEG based cameras using HTTP instead of VideoCapture - this should be a more CPU efficient method for low framerates
* Support for MQTT based override of camera parameters, such as requesting a single analysis when the camera is otherwise disabled


### Dependencies
This project requires the following dependencies:
* [AprilTag](https://github.com/aprilrobotics/apriltag) - You must install this according to their instructions. Make sure the python bindings are available. 
* Python modules: opencv-contrib-python, paho-mqtt, pyyaml