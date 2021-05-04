#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from cpp_pkg.msg import IntStr
from cpp_pkg.srv import BoolStr

class My_Publish(Node):

    def __init__(self):
        super().__init__("Int_publisher")
        self.get_logger().info("Pub_Node_Started_ok")


        self.i_will_publish_now = self.create_publisher(IntStr,"number",10) # Will Create the topic
        self.create_timer(1/1,self.timer_call)
        self.counter = 5

    def timer_call(self):
        New_var = IntStr()
        New_var.number = self.counter
        New_var.message = "5"

        self.get_logger().info(New_var.message)
        self.i_will_publish_now.publish(New_var)

def main (args=None):

    rclpy.init(args=args)
    node1 = My_Publish()
    rclpy.spin(node1)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
