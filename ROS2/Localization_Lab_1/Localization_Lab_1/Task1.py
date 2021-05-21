#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from math import sin, cos, pi
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Quaternion
from tf2_ros import TransformBroadcaster, TransformStamped
from sensor_msgs.msg import Imu
import numpy as np

class Task1(Node):
    def __init__(self):
        super().__init__("Task1")
        self.create_subscription(Imu, "/imu", self.listener_callback ,10)
        self.get_logger().info("subscriber is started")

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

    def listener_callback(self, msg):

        self.Sending_Var1 = self.euler_from_quaternion(msg.orientation)
        if -2 < self.Sending_Var1 < 2 :
            self.get_logger().info(" The robot is nearly heading north .. Heading is: {}  degrees ".format(self.Sending_Var1))

        if float(msg.linear_acceleration.x) < 0.3 :
            self.get_logger().info("Warning !! .. linear acceleration x exceeded the limit . Current acceleration is {}  m/s^2".format(msg.linear_acceleration.x))

        if float(msg.angular_velocity.z) < 0.3 :
            self.get_logger().info("Warning !! .. linear velocity z exceeded the limit . Current acceleration is {}  rad/sec".format(msg.angular_velocity.z))


def main (args=None):
    rclpy.init(args=args)
    node2 = Task1()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()