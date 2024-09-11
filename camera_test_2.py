import numpy as np
import pyzed.sl as sl
import cv2
import tensorflow as tf

def main():
    # Initialize the camera
    zed = sl.Camera()

    # Set initialization parameters
    init_params = sl.InitParameters()
    init_params.depth_mode = sl.DEPTH_MODE.ULTRA

    # Open the camera
    status = zed.open(init_params)
    if status != sl.ERROR_CODE.SUCCESS:
        print(f"Failed to open camera: {status}")
        return

    # Get and print camera information
    camera_info = zed.get_camera_information()
    print(f"Camera Model: {camera_info.camera_model}")
    print(f"Serial Number: {camera_info.serial_number}")
    print(f"Resolution: {camera_info.camera_configuration.resolution.width}x{camera_info.camera_configuration.resolution.height}")
    print(f"Camera FPS: {camera_info.camera_configuration.fps}")

    # Set object detection parameters
    obj_param = sl.ObjectDetectionParameters()
    obj_param.detection_model = sl.OBJECT_DETECTION_MODEL.MULTI_CLASS_BOX_FAST  # Use a different model
    obj_param.enable_tracking = False  # Disable tracking

    # Enable object detection
    returned_state = zed.enable_object_detection(obj_param)
    print(f"enable_object_detection: {returned_state}")
    if returned_state != sl.ERROR_CODE.SUCCESS:
        print(f"Error enabling object detection: {repr(returned_state)}")
        zed.close()
        return

    print("Object detection enabled successfully")

    # Close the camera
    zed.close()

if __name__ == "__main__":
    main()