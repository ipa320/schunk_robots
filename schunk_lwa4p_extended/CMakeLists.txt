cmake_minimum_required(VERSION 2.8.3)
project(schunk_lwa4p_extended)

find_package(catkin REQUIRED COMPONENTS roslaunch rostest)

catkin_package(
    CATKIN_DEPENDS xacro rostopic topic_tools cob_description schunk_description cob_command_gui cob_dashboard diagnostic_aggregator
    robot_state_publisher controller_manager cob_control_mode_adapter joint_state_controller position_controllers velocity_controllers
    joint_trajectory_controller cob_twist_controller cob_frame_tracker canopen_motor_node gazebo_ros cob_gazebo_ros_control cob_controller_configuration_gazebo
)

### TESTING ###
if(CATKIN_ENABLE_TESTING)
    roslaunch_add_file_check(launch)
    add_rostest(urdf/test/urdf.test)
endif()

### INSTALL ###
install(DIRECTORY config launch urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
