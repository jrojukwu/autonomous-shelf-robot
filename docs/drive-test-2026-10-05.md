# Headless drive test — October 5, 2026

Environment: Azure Ubuntu VM, ROS 2 Humble.

## Launch
ros2 launch shelf_description gazebo.launch.py gui:=false

## Verified results
- joint_state_broadcaster: active
- diff_drive_controller: active
- Command topic: /diff_drive_controller/cmd_vel_unstamped
- Message type: geometry_msgs/msg/Twist
- Forward command: linear.x = 0.1 m/s, angular.z = 0.0
- After the test, odometry position: x = 0.211686 m, y = -0.000336 m.
- A zero-velocity command was published.
- Subsequent reported velocity: linear.x = -0.000490 m/s,
  angular.z = -0.000375 rad/s, effectively stopped.

This verifies basic commanded motion and stopping through wheel odometry.
No laser-scan topic was present in the observed topic list.
Navigation and shelf detection were not tested in this session.
