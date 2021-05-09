#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Kill
from turtlesim.srv import Spawn
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from random import randint

'''
class My_Spawn(Node):

    def __init__(self):
        super().__init__("spawn_node")

    def service_client(self,data_msg):

        self.client_obj = self.create_client(Kill,"Spawn_Kill")

        while self.client_obj.wait_for_service(1)==False:
            self.get_logger().warn("wating for server")

        self.request = Spawn()
        self.request.x = randint(0,7)
        self.request.y = randint(0,7)



        self.future_obj = self.client_obj.call_async(self.request)
        self.future_obj.add_done_callback(self.future_call)
        
    def future_call(self,future_msg):
        self.get_logger().info(future_msg.result().message)
'''



def main (args=None):
    rclpy.init(args=args)
    node2 = My_Spawn()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
