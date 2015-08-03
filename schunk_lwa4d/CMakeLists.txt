cmake_minimum_required(VERSION 2.8.3)
project(schunk_lwa4d)

find_package(catkin REQUIRED COMPONENTS roslaunch rostest)

catkin_package(
    CATKIN_DEPENDS canopen_motor_node cob_command_gui cob_control_mode_adapter cob_controller_configuration_gazebo cob_dashboard cob_description cob_frame_tracker cob_gazebo_ros_control cob_twist_controller controller_manager diagnostic_aggregator gazebo_ros joint_state_controller joint_trajectory_controller position_controllers robot_state_publisher rostopic schunk_description topic_tools velocity_controllers xacro
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
