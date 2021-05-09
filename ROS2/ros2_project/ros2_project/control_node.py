#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import Kill
from turtlesim.srv import Spawn
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import sqrt , atan2
from random import randint


class My_Control(Node):
    def __init__(self):
        super().__init__("control_node")
        self.create_subscription(Pose,"turtle1/pose",self.Control_Call,10)
        self.get_logger().info("subscriber is started")
        self.i_will_publish_now = self.create_publisher(Twist,"turtle1/cmd_vel",10)  
    #    self.create_service(Spawn,"Spawn_Kill",self.Spawn_Call)

        self.P_lin = 0.5
        self.P_ang = 2

    #def Spawn_Call(self, request , response ):

    #    self.new_x = request.x # As Example
    #    self.new_y = request.y # As Example




    def Control_Call(self,msg):

        #___X___#
        self.current_x = msg.x
        self.get_logger().info(str(self.current_x))
        self.new_x = 2 # As Example
        self.x_error = self.new_x - self.current_x

        #___Y___#
        self.current_y = msg.y
        self.get_logger().info(str(self.current_y))
        self.new_y = 2 # As Example
        self.y_error = self.new_y - self.current_y

        #___linear_Vel___#
        self.linear_dist = abs(sqrt( ((self.y_error)**2)) + ((self.x_error)**2))
        self.lin_vel = self.linear_dist * self.P_lin

        #___theta___#
        self.current_theta = msg.theta
        self.get_logger().info(str(self.current_theta))
        self.new_theta = atan2 ( self.y_error , self.x_error )
        self.theta_error = self.new_theta - self.current_theta

        #___Angular_Vel___#
        self.ang_vel = self.theta_error * self.P_ang

        #___Publisher_Started___#  ros2 interface proto geometry_msgs/msg/Twist
        self.Pub_Var = Twist()
        self.Pub_Var.linear.x = self.lin_vel
        self.Pub_Var.angular.z = self.ang_vel
        self.i_will_publish_now.publish(self.Pub_Var)

        

def main (args=None):

    rclpy.init(args=args)
    node1 = My_Control()
    rclpy.spin(node1)
    rclpy.shutdown()

if __name__ == "__main__":
    main()