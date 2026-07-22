from launch import LaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

import os
import xacro


def generate_launch_description():
    package_name = "shelf_description"
    package_share = get_package_share_directory(package_name)

    xacro_file = os.path.join(
        package_share,
        "urdf",
        "shelf_robot.urdf.xacro",
    )

    controllers_file = os.path.join(
        package_share,
        "config",
        "controllers.yaml",
    )

    robot_description = xacro.process_file(xacro_file).toxml()

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[
            {"robot_description": robot_description},
            {"use_sim_time": False},
        ],
    )

    controller_manager = Node(
        package="controller_manager",
        executable="ros2_control_node",
        output="screen",
        parameters=[
            {"robot_description": robot_description},
            controllers_file,
        ],
    )

    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
        output="screen",
    )

    diff_drive_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "diff_drive_controller",
            "--controller-manager",
            "/controller_manager",
        ],
        output="screen",
    )

    start_diff_drive_after_joint_state = RegisterEventHandler(
        OnProcessExit(
            target_action=joint_state_broadcaster_spawner,
            on_exit=[diff_drive_controller_spawner],
        )
    )

    return LaunchDescription(
        [
            robot_state_publisher,
            controller_manager,
            joint_state_broadcaster_spawner,
            start_diff_drive_after_joint_state,
        ]
    )
