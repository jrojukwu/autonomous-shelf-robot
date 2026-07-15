import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/azureuser/autonomous-shelf-robot/ros2_ws/install/shelf_state_machine'
