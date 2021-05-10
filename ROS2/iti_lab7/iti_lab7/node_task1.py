#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from turtlesim.msg import Pose


class My_Task1(Node):

    def __init__(self):
        super().__init__("node_task1")
        self.create_subscription(String, "my_topic", self.listener_callback ,rclpy.qos.qos_profile_sensor_data)
        self.get_logger().info("subscriber is started")
        self.counter = 0

    def listener_callback(self, msg):
        self.counter += 1
        self.get_logger().info(" Moamen Heard {0} , {1} times".format(msg.data , self.counter))

def main (args=None):
    rclpy.init(args=args)
    node2 = My_Task1()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
