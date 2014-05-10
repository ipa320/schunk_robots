cmake_minimum_required(VERSION 2.8.3)
project(schunk_demo)
find_package(catkin REQUIRED COMPONENTS rospy cob_script_server pr2_controllers_msgs)

catkin_package(
    DEPENDS rospy cob_script_server pr2_controllers_msgs
)