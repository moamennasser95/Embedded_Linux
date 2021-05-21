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

class Task2(Node):
    def __init__(self):
        super().__init__("Task2")
        self.i_will_publish_now = self.create_publisher(Imu,"zed2_imu",10)
        self.create_timer(1/30,self.timer_call)

        with open('imu_data.csv', newline='') as file:
            reader = csv.reader(file)
            self.your_list = list(reader)
        
        self.counter = 0

    def timer_call(self):

        self.Pub_Var = Imu()
        #header
        self.Pub_Var.header.frame_id= "zed2_imu_link"
        #self.Pub_Var.header.stamp= self.Node.get_clock().now().to_msg()
        #linear_acceleration
        self.Pub_Var.linear_acceleration.x = float(self.your_list[self.counter][0])
        self.Pub_Var.linear_acceleration.y = float(self.your_list[self.counter][1])
        self.Pub_Var.linear_acceleration.z = float(self.your_list[self.counter][2])
        #linear_acceleration_covariance
        self.Pub_Var.linear_acceleration_covariance=[0.01, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.001]
        #angular_velocity
        self.Pub_Var.angular_velocity.x = float(self.your_list[self.counter][3])
        self.Pub_Var.angular_velocity.y = float(self.your_list[self.counter][4])
        self.Pub_Var.angular_velocity.z = float(self.your_list[self.counter][5])
        #orientation
        self.Pub_Var.orientation = self.quaternion_from_euler(0,0,float(self.your_list[self.counter][6]))

        if float(self.Pub_Var.angular_velocity.z) < 0.3 :
            #angular_velocity_covariance
            self.Pub_Var.angular_velocity_covariance = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 ]
            #orientation_covariance
            self.Pub_Var.orientation_covariance = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0 ]

        else :
            #angular_velocity_covariance
            self.Pub_Var.angular_velocity_covariance = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0 ]
            #orientation_covariance
            self.Pub_Var.orientation_covariance = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0 ]

        print(self.Pub_Var)
        self.i_will_publish_now.publish(self.Pub_Var)
        self.counter += 1

    def quaternion_from_euler(self, roll, pitch, yaw):
        qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
        qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
        qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
        qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
        return Quaternion(x=qx, y=qy, z=qz, w=qw)


def main (args=None):
    rclpy.init(args=args)
    node2 = Task2()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()