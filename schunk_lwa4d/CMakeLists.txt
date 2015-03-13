cmake_minimum_required(VERSION 2.8.3)
project(schunk_lwa4d)

find_package(catkin REQUIRED COMPONENTS roslaunch rostest)

catkin_package(
    CATKIN_DEPENDS cob_command_gui cob_dashboard joy cob_teleop robot_state_publisher cob_trajectory_controller gazebo_ros rostopic diagnostic_aggregator controller_manager
)

# test
if(CATKIN_ENABLE_TESTING)
    roslaunch_add_file_check(launch)
    add_rostest(urdf/test/urdf.test)
endif(CATKIN_ENABLE_TESTING)

# install
install(DIRECTORY calibration
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY config
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
