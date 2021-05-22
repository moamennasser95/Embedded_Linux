#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from math import sin, cos, pi
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Quaternion
from tf2_ros import TransformBroadcaster, TransformStamped
from sensor_msgs.msg import Imu
import numpy as np
from example_interfaces.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import csv
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from sensor_msgs.msg import NavSatFix

class Task1_Odom(Node):
    def __init__(self):
        super().__init__("Task1_Odom")

        self.create_subscription(Odometry, "/odom", self.listener_callback ,10)
        self.get_logger().info("Subscriber Is Started")

        with open('pose.csv', newline='') as file:
            reader = csv.reader(file)
            self.your_list = list(reader)
        
        self.counter = 1
        
    def listener_callback(self, msg):
        
        self.pose_x = float(self.your_list[self.counter][0])
        self.pose_y = float(self.your_list[self.counter][1])
        self.pose_yaw = float(self.your_list[self.counter][2])

        self.yaw_val = (self.euler_from_quaternion( msg.pose.pose.orientation)*180 ) / 3.14
        #print( msg.pose.pose.position.x , msg.pose.pose.position.y , self.yaw_val )

        self.current_pose_x_small = float(msg.pose.pose.position.x) - 0.5
        self.current_pose_x_large = float(msg.pose.pose.position.x) + 0.5
        self.current_pose_y_small = float(msg.pose.pose.position.y) - 0.5
        self.current_pose_y_large = float(msg.pose.pose.position.x) + 0.5
        self.current_pose_yaw_small = float(self.yaw_val) - 5
        self.current_pose_yaw_large = float(self.yaw_val) + 5


        if self.current_pose_x_small < self.pose_x < self.current_pose_x_large and self.current_pose_y_small < self.pose_y < self.current_pose_y_large and self.current_pose_yaw_small < self.pose_yaw < self.current_pose_yaw_large and self.counter == 1 :
            print("We Reach Position Number {} ".format(self.counter))
            self.counter += 1
            self.pose_x = float(self.your_list[self.counter][0])
            self.pose_y = float(self.your_list[self.counter][1])
            self.pose_yaw = float(self.your_list[self.counter][2])

        if self.current_pose_x_small < self.pose_x < self.current_pose_x_large and self.current_pose_y_small < self.pose_y < self.current_pose_y_large and self.current_pose_yaw_small < self.pose_yaw < self.current_pose_yaw_large and self.counter == 2 :
            print("We Reach Position Number {} ".format(self.counter))
            self.counter += 1
            self.pose_x = float(self.your_list[self.counter][0])
            self.pose_y = float(self.your_list[self.counter][1])
            self.pose_yaw = float(self.your_list[self.counter][2])

        if self.current_pose_x_small < self.pose_x < self.current_pose_x_large and self.current_pose_y_small < self.pose_y < self.current_pose_y_large and self.current_pose_yaw_small < self.pose_yaw < self.current_pose_yaw_large and self.counter == 3 :
            print("We Reach Position Number {} ".format(self.counter))
            self.counter += 1
            self.pose_x = float(self.your_list[self.counter][0])
            self.pose_y = float(self.your_list[self.counter][1])
            self.pose_yaw = float(self.your_list[self.counter][2])

        if self.current_pose_x_small < self.pose_x < self.current_pose_x_large and self.current_pose_y_small < self.pose_y < self.current_pose_y_large and self.current_pose_yaw_small < self.pose_yaw < self.current_pose_yaw_large and self.counter == 4 :
            print("We Reach Position Number {} ".format(self.counter))
            self.counter += 1
            print(f'i execute all position and last one is {msg.pose.pose.position.x} , {msg.pose.pose.position.y} , {self.yaw_val}')



    def euler_from_quaternion(self, quaternion):
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w
        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)
        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)
        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)
        return yaw 


def main (args=None):
    rclpy.init(args=args)
    node2 = Task1_Odom()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()





'''

        if (float(msg.pose.pose.position.x)+0.5) >= (float(self.your_list[self.counter][0]) >= (float(msg.pose.pose.position.x)-0.5) \
            and (float(msg.pose.pose.position.y)+0.5) >= (float(self.your_list[self.counter][1]) >= (float(msg.pose.pose.position.y)-0.5) \
            and (float(self.yaw_val)+5) >= (float(self.your_list[self.counter][2])) >= (float(self.yaw_val)-5) :

                print("Hello")

'''