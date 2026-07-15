from pathlib import Path

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    package_share = Path(get_package_share_directory("shelf_description"))
    xacro_file = package_share / "urdf" / "shelf_robot.urdf.xacro"
    rviz_file = package_share / "rviz" / "shelf_robot.rviz"

    robot_description = {
        "robot_description": Command(["xacro ", str(xacro_file)])
    }

    return LaunchDescription(
        [
            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[robot_description],
                output="screen",
            ),
            Node(
                package="joint_state_publisher_gui",
                executable="joint_state_publisher_gui",
                output="screen",
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                arguments=["-d", str(rviz_file)],
                output="screen",
            ),
        ]
    )
