export TURTLEBOT3_MODEL=burger(or waffle or waffle_pi)

# waffle相機影像：
rosrun image_view image_view image:=/camera/rgb/image_raw

# 執行yolo:
roslaunch darknet_ros yolo_v3.launch
darknet_ros/darknet_ros/config/ros.yaml可調整輸入影像的topic

# 鍵盤操控TURTLEBOT：
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

# 打開自製world:
roslaunch turtlebot3_gazebo self_world.launch
roslaunch turtlebot3_gazebo self_world2.launch


# zedm run rtabmap(use zedm odom):
roslaunch zed_wrapper zed_camera.launch
roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start" frame_id:=zed_camera_center approx_sync:=false visual_odometry:=false odom_topic:=/zed_node/odom rgb_topic:=/zed_node/rgb/image_rect_color depth_topic:=/zed_node/depth/depth_registered camera_info_topic:=/zed_node/rgb/camera_info

# show rtabmap result:
rtabmap-databaseViewer ~/.ros/rtabmap.db

# print 2d grid map:
run rtabmap.launch than use rviz rviz to subscribe proj_map...etc
close rtabmap.launch than use rtabmap-databaseViewer file->export 2d map can get pgm map file

# 問題：
gazebo內雖然在world內能找到大部分的link(turtlebot3 base_footprint)但跑rosrun rtabmap_ros rgbd_odometry rgb/image:=/camera/rgb/image_r depth/image:=/camera/depth/image_raw rgb/camera_info:=/camera/rgb/camera_info _frame_id:=base_footprint時還是找不到camera_rgb_optical_frame

#功能：
rospack find [package名]



