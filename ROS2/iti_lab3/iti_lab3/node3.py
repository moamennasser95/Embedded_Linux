#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from cpp_pkg.msg import IntStr
from cpp_pkg.srv import BoolStr

class My_Client(Node):

    def __init__(self):
        super().__init__("reset_client")
        self.service_client(True)    

    def service_client(self,data_msg):
        self.client = self.create_client(BoolStr,"Reset_Server")

        while self.client.wait_for_service(1)==False:
            self.get_logger().warn("wating for server")

        self.request = BoolStr.Request()
        self.request.check = data_msg

        self.future = self.client.call_async(self.request)

        #response_variable = SetBool.Response()
        #response_variable = self.future.set_result(response_variable.message)
        #self.get_logger().info(str(response_variable))




def main (args=None):
    rclpy.init(args=args)
    node3 = My_Client()

    rclpy.spin_until_future_complete(node3,node3.future)
    response = node3.future.result()
    node3.get_logger().info(response.message)

    rclpy.shutdown()

if __name__ == "__main__":
    main()