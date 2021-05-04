#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from cpp_pkg.msg import IntStr
from cpp_pkg.srv import BoolStr

class My_Server(Node):
    
    NUM = 0
    def __init__(self):
        super().__init__("number_counter")

        self.create_subscription(IntStr, "number", self.timer_call, 10)
        self.get_logger().info("subscriber is started")
        self.pub_num = self.create_publisher(IntStr, "number_counter", 10)
        self.create_service(BoolStr, "Reset_Server", self.service_call)

    def timer_call(self, num):

        self.get_logger().info(str(self.NUM))
        self.NUM += num.number

        pub_int = IntStr()
        pub_int.number = self.NUM
        self.pub_num.publish(pub_int)
        
    #ros2 service call /Reset_Server example_interfaces/srv/SetBool "data: true"
    
    def service_call(self, rq, rsp):

        self.req = rq.check
        if self.req == True: 
            self.NUM = 0
            rsp.message = "OK_CALL"
        return rsp


def main (args=None):
    rclpy.init(args=args)
    node2 = My_Server()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
