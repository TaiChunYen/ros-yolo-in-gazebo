import rospy
import pdb
import sys
sys.path.append("/home/taita/catkin_ws/src/darknet_ros")
#pdb.set_trace()
from darknet_ros_msgs.msg import *

def callback(datas):
    rospy.loginfo(datas.bounding_boxes[0].probability)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
