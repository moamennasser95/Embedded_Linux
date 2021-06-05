#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Path
import math
import numpy as np
  
class LAB4_planning(Node):
    def __init__(self):
        super().__init__("LAB4_planning")
        self.create_subscription(Path, "/local_plan", self.timer_call,10)
        self.get_logger().info("subscriber is started")

    def menger_curvature(self, point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y):
        triangle_area = 0.5 * abs( (point_1_x*point_2_y) + (point_2_x*point_3_y) + (point_3_x*point_1_y) - (point_2_x*point_1_y) - (point_3_x*point_2_y) - (point_1_x*point_3_y))#Shoelace formula 
        
        try:
            curvature = (4*triangle_area) / (math.sqrt(pow(point_1_x - point_2_x,2)+pow(point_1_y - point_2_y,2)) * math.sqrt(pow(point_2_x - point_3_x,2)+pow(point_2_y - point_3_y,2)) * math.sqrt(pow(point_3_x - point_1_x,2)+pow(point_3_y - point_1_y,2)))#Menger curvature 
            return curvature
        except:
            return 0 
        

    def euler_from_quaternion(self, quaternion):
        x = quaternion.x
        y = quaternion.y
        z = quaternion.z
        w = quaternion.w
        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = np.arctan2(sinr_cosp, cosr_cosp)
        sinp = 2 * (w * y - z * x)
        pitch = np.arcsin(sinp)
        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = np.arctan2(siny_cosp, cosy_cosp)
        return yaw  

    def timer_call(self, msg):
        point_1_x = msg.poses[0].pose.position.x
        point_1_y = msg.poses[0].pose.position.y
        point_2_x = msg.poses[5].pose.position.x
        point_2_y = msg.poses[5].pose.position.y
        point_3_x = msg.poses[10].pose.position.x
        point_3_y = msg.poses[10].pose.position.y

        ret_fun = self.menger_curvature(point_1_x, point_1_y, point_2_x, point_2_y, point_3_x, point_3_y)
        ret_yaw = self.euler_from_quaternion( msg.poses[0].pose.orientation )
        
        #self.get_logger().info("The path is straight  :{}".format(ret_fun))
        #self.get_logger().info(" Yaw  :{}".format(ret_yaw))

        if ret_fun < 1.3 :
            self.get_logger().info("The path is straight")
        elif ret_yaw > 0 :
            self.get_logger().info("The robot is turning to the right with a curvature " + str(ret_fun))
        elif ret_yaw < 0 :
            self.get_logger().info("The robot is turning to the left with a curvature " + str(ret_fun))



def main (args=None):
    rclpy.init(args=args)
    node2 = LAB4_planning()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()