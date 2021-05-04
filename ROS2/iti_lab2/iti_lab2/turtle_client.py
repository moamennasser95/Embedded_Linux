#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

class Turtle_Client(Node):

    def __init__(self):
        super().__init__("client_node")

        self.service_client()    

    def service_client(self):

        self.client = self.create_client(Empty,"/reset")

        while self.client.wait_for_service(1)==False:
            self.get_logger().warn("wating for server")

        self.request = Empty.Request()

        self.future = self.client.call_async(self.request)



def main (args=None):
    rclpy.init(args=args)
    turtle_client = Turtle_Client()
    rclpy.spin(turtle_client)
    rclpy.shutdown()

if __name__ == "__main__":
    main()