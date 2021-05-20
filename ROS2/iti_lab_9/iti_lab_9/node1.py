#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import csv
from turtlesim.msg import Pose
from std_srvs.srv import Empty 


class My_Publisher(Node):
    def __init__(self):
        super().__init__("Publisher")
        self.get_logger().info("Publisher_Node_Started_ok")

        self.i_will_publish_now = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_timer(1/1,self.timer_call)

        self.create_subscription(Pose, "/turtle1/pose", self.listener_callback ,10)
        
        self.client_obj = self.create_client(Empty,"Reset")

        with open('turtle_commands.csv', newline='') as file:
            reader = csv.reader(file)
            self.your_list = list(reader)

        self.counter = 1

    def timer_call(self):
        self.Pub_Var = Twist()

        self.Pub_Var.linear.x = float(self.your_list[self.counter][0])
        self.Pub_Var.angular.z = float(self.your_list[self.counter][1])

        self.i_will_publish_now.publish(self.Pub_Var)

        self.counter += 1

    def listener_callback(self, msg):

        if 2.00 > float(msg.x) or 8.00 < float(msg.x) or 2.00 > float(msg.y) or 8.00 < float(msg.y) :
            self.reset_callback()    

    def reset_callback(self):

        self.client = self.create_client(Empty,"/reset")

        while self.client.wait_for_service(1)==False:
            self.get_logger().warn("wating for server")

        self.request = Empty.Request()

        self.future = self.client.call_async(self.request)


def main (args=None):
    rclpy.init(args=args)
    node1 = My_Publisher()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
