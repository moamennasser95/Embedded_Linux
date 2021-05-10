#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class My_Task2(Node):
    def __init__(self):
        super().__init__("node_task2")
        self.create_subscription(Pose, "/turtle1/custom_pose", self.listener_callback ,rclpy.qos.qos_profile_sensor_data)
        self.get_logger().info("subscriber is started")

    def listener_callback(self, msg):
        print( msg.x , msg.y ) 

def main (args=None):
    rclpy.init(args=args)
    node2 = My_Task2()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
