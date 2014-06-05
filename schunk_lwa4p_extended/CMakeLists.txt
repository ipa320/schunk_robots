cmake_minimum_required(VERSION 2.8.3)
project(schunk_lwa4p_extended)

find_package(catkin REQUIRED COMPONENTS)


# TODO: fill in what other packages will need to use this package
## DEPENDS: system dependencies of this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## INCLUDE_DIRS: 
## LIBRARIES: libraries you create in this project that dependent projects also need
catkin_package(
    CATKIN_DEPENDS  ipa_canopen_ros cob_command_gui cob_dashboard joy cob_teleop robot_state_publisher cob_trajectory_controller gazebo_ros rostopic diagnostic_aggregator pr2_dashboard_aggregator controller_manager 
    DEPENDS # TODO
    INCLUDE_DIRS # TODO include
    LIBRARIES # TODO
)


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
