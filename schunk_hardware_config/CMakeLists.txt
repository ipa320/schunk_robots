cmake_minimum_required(VERSION 2.8.3)
project(schunk_hardware_config)
find_package(catkin REQUIRED COMPONENTS roslaunch rostest cob_description schunk_description schunk_sdh schunk_powercube_chain)

# rostest
roslaunch_add_file_check(lwa/urdf)
add_rostest(lwa/test/urdf.test)

roslaunch_add_file_check(sdh/urdf)
add_rostest(sdh/test/urdf.test)

roslaunch_add_file_check(lwa4p/urdf)
add_rostest(lwa4p/test/urdf.test)

roslaunch_add_file_check(lwa4d/urdf)
add_rostest(lwa4d/test/urdf.test)

catkin_package(
    DEPENDS cob_description schunk_description schunk_sdh schunk_powercube_chain
)