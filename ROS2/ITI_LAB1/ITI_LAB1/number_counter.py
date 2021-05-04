#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int64
from example_interfaces.msg import Bool



class My_Sub(Node):
    def __init__(self):
        super().__init__("number_counter")

        self.get_logger().info("Subscriper Started")

        self.i_will_subscripe_now = self.create_subscription(String,"str_topic",self.sub_call,10) # Will Create the topic

        self.number_pub = self.create_publisher(Int64,"number",10)

        self.counter=0

        self.bool_obj = self.create_publisher(Bool,"reset_flag",10)


    def sub_call(self,msg):

        self.get_logger().info(msg.data)

        number = int(data.split(',')[1])

        msg_int = Int64()
        msg_int.data = number

        self.number_pub.publish(msg_int)

        if number >= 5 :
            
            msg_bool=Bool()
            msg_bool.data = True
            self.bool_obj.publish(msg_bool)





def main(args=None):
    rclpy.init(args=args) # To Start Communication ( this Step is Must in ROS )
    My_Node=My_Pub()        
    rclpy.spin(My_Node)  # 3shan el topic yfdal mwgod w mstany ab3tlo ay 7aga gdeda 

    rclpy.shutdown() # To End Communication ( this Step is Must in ROS )

if __name__=="__main__":
    main()