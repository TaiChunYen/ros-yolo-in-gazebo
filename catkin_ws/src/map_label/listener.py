import rospy
import pdb
import sys
sys.path.append("/home/taita/catkin_ws/src/darknet_ros")

from darknet_ros_msgs.msg import *
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
from sensor_msgs.msg import Image


class listener():

    def __init__(self):

        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, self.callback)
        rospy.Subscriber("/zed_node/depth/depth_registered", Image, self.callback_depth)

        self.u=None
        self.v=None

        self.fx = 699.618
        self.fy = 699.618
        self.cx = 611.475
        self.cy = 367.377

    def callback(self,datas):
        #rospy.loginfo(datas.bounding_boxes[0].probability)
        if datas.bounding_boxes[0].probability>0.5:
            self.u = (datas.bounding_boxes[0].xmin+datas.bounding_boxes[0].xmax)/2
            self.v = (datas.bounding_boxes[0].ymin+datas.bounding_boxes[0].ymax)/2
            print('bb: {width}x{height}'.format(width=self.u,height=self.v))

        elif datas.bounding_boxes[0].probability<0.5:
            self.u=None
            self.v=None

    def callback_depth(self,depth_data):
        bridge = CvBridge()
        try:
            depth_image = bridge.imgmsg_to_cv2(depth_data, "32FC1")
        except CvBridgeError as e:
            print(e)

        depth_array = np.array(depth_image, dtype=np.float32)
        #print('Image size: {width}x{height}'.format(width=depth_array.shape[0],height=depth_array.shape[1]))
        #print('Image size: {width}x{height}'.format(width=depth_data.width,height=depth_data.height))
           
        if self.u != None and self.v != None:
            print('Center depth: {dist} m'.format(dist=depth_array[self.v,self.u]))

            Z = depth_array[self.v,self.u]
            X = Z / self.fx * (self.u - self.cx)
            Y = Z / self.fy * (self.v - self.cy)
            print('world coordinate: {x},{y},{z}'.format(x=X,y=Y,z=Z))
    
        

if __name__ == '__main__':
    listener()
    rospy.spin()
    # spin() simply keeps python from exiting until this node is stopped
