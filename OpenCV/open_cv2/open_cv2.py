#!/usr/bin/env python3
import rclpy
import numpy as np
import math
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from matplotlib import pyplot as plt
bridge = CvBridge()
import time
from util import *


class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Image,"/intel_realsense_d435_depth/image_raw",self.img_cb, rclpy.qos.qos_profile_sensor_data)
        self.get_logger().info("subscriber is started")

        self.old_frame = cv2.imread('frame1.png')
        self.new_frame = 0

    def img_cb(self, message):

        cv2_img = bridge.imgmsg_to_cv2(message, "bgr8")
        gray = cv2.cvtColor(cv2_img,cv2.COLOR_BGR2GRAY)
        self.new_frame = np.copy(gray)

        orb = cv2.ORB_create()                                     ###########
        bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)           ###########
        kp1, ds1 = orb.detectAndCompute(self.old_frame, None)      ###########
        kp2, ds2 = orb.detectAndCompute(self.new_frame, None)      ###########

        if ds1 is not None and ds2 is not None:

            matches = bf.match(ds1,ds2)                             ##########
            matches = sorted(matches, key = lambda x:x.distance)    ##########
            list_kp1 = [kp1[mat.queryIdx].pt for mat in matches]    ##########
            list_kp2 = [kp2[mat.trainIdx].pt for mat in matches]    ##########

            delta_x = 0
            delta_y = 0

            for i in range(len(list_kp1)):
                delta_x += (int (list_kp1[i][0]) - int (list_kp2[i][0]))
                delta_y += (int (list_kp1[i][1]) - int (list_kp2[i][1]))
            if len(list_kp1) :    
                delta_x /= len(list_kp1)
                delta_y /= len(list_kp1)

            start_y , start_x = gray.shape
            start_x /= 2
            start_y /= 2

            x_and_y = ( int(start_x) , int(start_y) )
            next = ( int(start_x) + int(delta_x) , int(start_y) + int(delta_y) )  
            img = cv2.arrowedLine(cv2_img, x_and_y, next, (0,0,255) , 3)

            cv2.imshow("img", img)
            self.old_frame = np.copy( self.new_frame )

        if cv2.waitKey(1) & 0xff == 27:
            cv2.destroyAllWindows()



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()











