/**************************************************************************
 * @author z.h
 * @date 2019.1.4
 * @usage:image_subscribe.cpp 
 * @brief:@params[IN]:@return:
 **************************************************************************/
#include <ros/ros.h>
#include <opencv2/opencv.hpp>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>

void imageCallback(const sensor_msgs::ImageConstPtr& msg)
{
	try
	{
		cv::imshow("view", cv_bridge::toCvShare(msg, "bgr8")->image);
		cv::imwrite("/home/zxkj/catkin_darknet/src/detecting_test/data/results.jpg", cv_bridge::toCvShare(msg, "bgr8")->image);
		cv::waitKey(10);
	}
	catch (cv_bridge::Exception& e)
	{
		ROS_ERROR("Could not convert from '%s' to 'bgr8'.", msg->encoding.c_str());
	}
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "image_subscriber");
	ros::NodeHandle nh;
	cv::namedWindow("view");
	//cv::startWindowThread();
	image_transport::ImageTransport it(nh);
	image_transport::Subscriber sub = it.subscribe("/darknet_ros/detection_image", 1, imageCallback);///darknet_ros/detection_image
	ros::spin();
	cv::destroyWindow("view");
	return 0;
}
