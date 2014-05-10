cmake_minimum_required(VERSION 2.8.3)
project(schunk_controller_configuration_gazebo)
find_package(catkin REQUIRED COMPONENTS roslaunch rostopic pr2_controller_manager joint_trajectory_action schunk_simulated_tactile_sensors)

# rostest
roslaunch_add_file_check(ros/launch)

catkin_package(
    DEPENDS rostopic pr2_controller_manager joint_trajectory_action schunk_simulated_tactile_sensors
)