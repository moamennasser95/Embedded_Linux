#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class My_Server(Node):
    NUM = 0
    def __init__(self):
        super().__init__("STR_Subscriber")

        self.create_subscription(String, "hello", self.timer_call,10)
        self.get_logger().info("subscriber is started")

    def timer_call(self, msg):

        self.Write_msg = msg.data
        self.get_logger().info("I Heard " + str(self.Write_msg))

def main (args=None):
    rclpy.init(args=args)
    node2 = My_Server()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
