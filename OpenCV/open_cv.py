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

class my_node (Node):
    def __init__(self):
        super().__init__("sub_node")
        self.create_subscription(Image,"/intel_realsense_d435_depth/image_raw",self.img_cb, rclpy.qos.qos_profile_sensor_data)
        
        self.get_logger().info("subscriber is started")

    def img_cb(self,message):

        cv2_img = bridge.imgmsg_to_cv2(message, "bgr8")
        blank_image = np.zeros((240,320,1), np.uint8)
        gray = cv2.cvtColor(cv2_img,cv2.COLOR_BGR2GRAY)
        #print(cv2_img.shape)

        time1 = time.time()
        corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
        time2 = time.time() - time1
        print(time2)

        corners = np.int0(corners)

        if len(corners) >= 1 :

            for i in corners:
                print(i)
                x,y = i.ravel()
                cv2.circle(blank_image,(x,y),3,255,-1)

            cv2.imshow("cv2_img", cv2_img)
            cv2.imshow("blank", blank_image)
        

        if cv2.waitKey(1) & 0xff == 27:
            cv2.destroyAllWindows()  



def main (args=None):
    rclpy.init(args=args)
    node=my_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()