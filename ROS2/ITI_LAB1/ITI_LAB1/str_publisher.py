#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Bool



class My_Pub(Node):
    def __init__(self):
        super().__init__("str_publisher")

        self.get_logger().info("Publisher Started")

        self.i_will_publish_now = self.create_publisher(String,"str_topic",10) # Will Create the topic

        self.create_timer(1/1,self.timer_call)

        self.counter=0

        self.create_subscription(Bool,"reset_flag",self.reset_call,10)
        

    def timer_call(self):

        msg_str = String()

        msg_str.data = "Moamen is Publish , {} ".format(self.counter)


        
        self.i_will_publish_now.publish(msg_str)
        self.counter+=1

    def reset_call(self,)
        if bool_msg.data == True:
            self.counter=0




def main(args=None):
    rclpy.init(args=args) # To Start Communication ( this Step is Must in ROS )
    My_Node=My_Pub()        
    rclpy.spin(My_Node)  # 3shan el topic yfdal mwgod w mstany ab3tlo ay 7aga gdeda 

    rclpy.shutdown() # To End Communication ( this Step is Must in ROS )

if __name__=="__main__":
    main()