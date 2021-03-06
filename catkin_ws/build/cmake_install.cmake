# Install script for directory: /home/taita/catkin_ws/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/taita/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/taita/catkin_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/taita/catkin_ws/install" TYPE PROGRAM FILES "/home/taita/catkin_ws/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/taita/catkin_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/taita/catkin_ws/install" TYPE PROGRAM FILES "/home/taita/catkin_ws/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "/home/taita/catkin_ws/install/setup.bash;/home/taita/catkin_ws/install/local_setup.bash")
=======
   "/home/taita/catkin_ws/install/setup.bash")
>>>>>>> 1e3ce309e3138c1191960b800eae7ed9ffe06b7d
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
<<<<<<< HEAD
file(INSTALL DESTINATION "/home/taita/catkin_ws/install" TYPE FILE FILES
    "/home/taita/catkin_ws/build/catkin_generated/installspace/setup.bash"
    "/home/taita/catkin_ws/build/catkin_generated/installspace/local_setup.bash"
    )
=======
file(INSTALL DESTINATION "/home/taita/catkin_ws/install" TYPE FILE FILES "/home/taita/catkin_ws/build/catkin_generated/installspace/setup.bash")
>>>>>>> 1e3ce309e3138c1191960b800eae7ed9ffe06b7d
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "/home/taita/catkin_ws/install/setup.sh;/home/taita/catkin_ws/install/local_setup.sh")
=======
   "/home/taita/catkin_ws/install/setup.sh")
>>>>>>> 1e3ce309e3138c1191960b800eae7ed9ffe06b7d
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
<<<<<<< HEAD
file(INSTALL DESTINATION "/home/taita/catkin_ws/install" TYPE FILE FILES
    "/home/taita/catkin_ws/build/catkin_generated/installspace/setup.sh"
    "/home/taita/catkin_ws/build/catkin_generated/installspace/local_setup.sh"
    )
=======
file(INSTALL DESTINATION "/home/taita/catkin_ws/install" TYPE FILE FILES "/home/taita/catkin_ws/build/catkin_generated/installspace/setup.sh")
>>>>>>> 1e3ce309e3138c1191960b800eae7ed9ffe06b7d
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
<<<<<<< HEAD
   "/home/taita/catkin_ws/install/setup.zsh;/home/taita/catkin_ws/install/local_setup.zsh")
=======
   "/home/taita/catkin_ws/install/setup.zsh")
>>>>>>> 1e3ce309e3138c1191960b800eae7ed9ffe06b7d
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
<<<<<<< HEAD
file(INSTALL DESTINATION "/home/taita/catkin_ws/install" TYPE FILE FILES
    "/home/taita/catkin_ws/build/catkin_generated/installspace/setup.zsh"
    "/home/taita/catkin_ws/build/catkin_generated/installspace/local_setup.zsh"
    )
=======
file(INSTALL DESTINATION "/home/taita/catkin_ws/install" TYPE FILE FILES "/home/taita/catkin_ws/build/catkin_generated/installspace/setup.zsh")
>>>>>>> 1e3ce309e3138c1191960b800eae7ed9ffe06b7d
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/taita/catkin_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/taita/catkin_ws/install" TYPE FILE FILES "/home/taita/catkin_ws/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/taita/catkin_ws/build/gtest/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3/turtlebot3/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3_msgs/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3/turtlebot3_navigation/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3_simulations/turtlebot3_simulations/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/darknet_ros/darknet_ros_msgs/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/darknet_ros/darknet_ros/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/detecting_test/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3/turtlebot3_bringup/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3/turtlebot3_example/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3_simulations/turtlebot3_fake/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3_simulations/turtlebot3_gazebo/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3/turtlebot3_slam/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3/turtlebot3_teleop/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/turtlebot3/turtlebot3_description/cmake_install.cmake")
<<<<<<< HEAD
  include("/home/taita/catkin_ws/build/zed-ros-wrapper/examples/zed_ar_track_alvar_example/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/zed-ros-wrapper/tutorials/zed_depth_sub_tutorial/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/zed-ros-wrapper/zed_display_rviz/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/zed-ros-wrapper/examples/zed_nodelet_example/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/zed-ros-wrapper/zed_ros/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/zed-ros-wrapper/examples/zed_rtabmap_example/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/zed-ros-wrapper/tutorials/zed_tracking_sub_tutorial/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/zed-ros-wrapper/tutorials/zed_video_sub_tutorial/cmake_install.cmake")
  include("/home/taita/catkin_ws/build/zed-ros-wrapper/zed_wrapper/cmake_install.cmake")
=======
>>>>>>> 1e3ce309e3138c1191960b800eae7ed9ffe06b7d

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/taita/catkin_ws/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
