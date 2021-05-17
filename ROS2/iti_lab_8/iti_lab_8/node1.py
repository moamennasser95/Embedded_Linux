#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class My_Publish(Node):

    def __init__(self):
        super().__init__("Int_publisher")
        self.get_logger().info("Pub_Node_Started_ok")

        self.i_will_publish_now = self.create_publisher(String,"hello",10)

        self.create_timer(1/1,self.timer_call)
        self.counter = 0

    def timer_call(self):

        var = String()

        if self.counter % 2 == 0:
            var.data = "Hi"

        elif self.counter % 2 ==1:
            var.data = "Hello"

        self.counter += 1

        self.get_logger().info(str(var.data))
        self.i_will_publish_now.publish(var)




def main (args=None):

    rclpy.init(args=args)
    node1 = My_Publish()
    rclpy.spin(node1)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
