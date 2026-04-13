from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. The USB Camera Node with hardcoded parameters
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            parameters=[
                {'video_device': '/dev/video22'},
                {'framerate': 30.0}
            ]
        ),
        
        # 2. Your custom Face Tracker Node
        Node(
            package='face_tracker',
            executable='face_tracker',
            name='face_tracker_node'
        )
    ])
