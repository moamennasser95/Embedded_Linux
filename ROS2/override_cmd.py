#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import csv
import math
from turtlesim.msg import Pose
from std_srvs.srv import Empty 
from sensor_msgs.msg import LaserScan
import numpy as np


class My_Publisher(Node):
    def __init__(self):
        super().__init__("My_Publisher")
        self.get_logger().info("Publisher_Node_Started_ok")

        self.i_will_publish_now = self.create_publisher(Twist,"/cmd_vel",10)
        self.create_timer(1/20,self.timer_call)

        self.create_subscription(Twist, "/key_cmd_vel", self.listener_callback ,10)

        self.create_subscription(LaserScan, "/scan", self.scan_cb, rclpy.qos.qos_profile_sensor_data)

    def listener_callback(self, msg):

        self.sub_msg = msg


    def scan_cb(self,message):

        laser_data = message.ranges
        self.min_value = min(laser_data[0 : 30] + laser_data[330 : 360])
        print(self.min_value)


    def timer_call(self):

        any_var = self.min_value
        
        if any_var > 1 :
            self.i_will_publish_now.publish(self.sub_msg)
        else:
            self.i_will_publish_now.publish(0)
            print("Robot has been stuck ")
        

def main (args=None):
    rclpy.init(args=args)
    node1 = My_Publisher()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()














        # Var = Twist()
        # Var.linear.x = 0.0
        # Var.angular.z = 0.0