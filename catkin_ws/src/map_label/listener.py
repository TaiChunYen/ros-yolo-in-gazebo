import rospy
import pdb
import sys
sys.path.append("/home/taita/catkin_ws/src/darknet_ros")

from darknet_ros_msgs.msg import *
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from sensor_msgs.msg import Image

def callback(datas):
    rospy.loginfo(datas.bounding_boxes[0].probability)

def callback_depth(depth_data):
    bridge = CvBridge()
    try:
        depth_image = bridge.imgmsg_to_cv2(depth_data, "32FC1")
    except CvBridgeError as e:
        print(e)

    depth_array = np.array(depth_image, dtype=np.float32)
    print('Image size: {width}x{height}'.format(width=depth_data.width,height=depth_data.height))
    
    u = depth_data.width/2
    v = depth_data.height/2
    print('Center depth: {dist} m'.format(dist=depth_array[u,v]))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, callback)

    rospy.Subscriber("/zed_node/depth/depth_registered", Image, callback_depth)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
