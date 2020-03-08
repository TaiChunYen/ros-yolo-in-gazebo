# 模擬環境：

export TURTLEBOT3_MODEL=waffle(or burger or waffle_pi)

## waffle相機影像：
rosrun image_view image_view image:=/camera/rgb/image_raw

## 執行yolo:
roslaunch darknet_ros yolo_v3.launch  
darknet_ros/darknet_ros/config/ros.yaml可調整輸入影像的topic  
(/camera/rgb/image_raw)

## 鍵盤操控TURTLEBOT：
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

## 打開自製world:
roslaunch turtlebot3_gazebo apple.launch  
roslaunch turtlebot3_gazebo self_world.launch  
roslaunch turtlebot3_gazebo self_world2.launch  
* 自製貼圖model:  
https://blog.csdn.net/zyh821351004/article/details/49785855  
* model static:  
http://answers.gazebosim.org/question/13547/how-to-make-a-object-static-in-gazebo/  

## rtabmap在自製world運行：
roslaunch turtlebot3_gazebo self_world2.launch  
(還沒在self_world.launch內加入robot_state_publisher)  
rviz rviz global options的fix frame改成base_footprint  
roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start" frame_id:=base_footprint rgb_topic:=/camera/rgb/image_raw depth_topic:=/camera/depth/image_raw camera_info_topic:=/camera/rgb/camera_info  visual_odometry:=false odom_topic:=/odom

## rosbag:
* record:  
roslaunch turtlebot3_gazebo passion.launch  
rosbag record /camera/rgb/camera_info /camera/rgb/image_raw/comessed /camera/rgb/image_raw/compressedDepth /odom /tf /tf_static  

* play:  
roslaunch passion_bag.launch  
roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start" frame_id:=base_footprint rgb_topic:=/camera/data depth_topic:=/camera/depth/image_raw camera_info_topic:=/camera/rgb/camera_info  visual_odometry:=false odom_topic:=/odom subscribe_scan:=false  

## find object with yolo and label on map:
roslaunch passion_find.launch  
(reference:https://github.com/TaiChunYen/find_object_yolo)  

# 真實環境

## 執行yolo:
roslaunch darknet_ros yolo_v3.launch  
darknet_ros/darknet_ros/config/ros.yaml可調整輸入影像的topic  
(/zed_node/rgb/image_rect_color)

## zedm run rtabmap(use zedm odom):
roslaunch zed_wrapper zed_camera.launch  
roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start" frame_id:=zed_camera_center approx_sync:=false visual_odometry:=false odom_topic:=/zed_node/odom rgb_topic:=/zed_node/rgb/image_rect_color depth_topic:=/zed_node/depth/depth_registered camera_info_topic:=/zed_node/rgb/camera_info

## show rtabmap result:
rtabmap-databaseViewer ~/.ros/rtabmap.db

## print 2d grid map:
method1.  
run rtabmap.launch than use rviz rviz to subscribe proj_map  
close rtabmap.launch than use rtabmap-databaseViewer file->export 2d map can get pgm map file  
method2.  
rosrun map_server map_saver map:=/rtabmap/proj_map  

## get distance and world coordinate:
cd ./src/map_label  
python2.7 listener.py  
* zed camera intrinsics:  
https://support.stereolabs.com/hc/en-us/articles/360007497173-What-is-the-calibration-file-
* turtlebot3 camera intrinsics:  
rostopic echo /camera/rgb/camera_info     
K = [fx 0 cx 0 fy cy 0 0 1]    
* turtlebot3不知為何是定位到載具而非物品  

## pgm to jpg:
cd ./src/map_label  
python2.7 pgm2jpg.py -i [input pgm name] -o [output jpg name]  
example:  
python2.7 pgm2jpg.py -i map.pgm -o map.jpg  
* 調整py裡的圖片大小  

## print object label on map:
cd ./src/map_label  
python2.7 map_label.py  

# 測試常用指令：
rospack find [package名]  
rosrun rqt_tf_tree rqt_tf_tree  
rostopic type [topic]  
ls /dev(看裝置有無被電腦讀取)



