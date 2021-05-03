#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

# int   + - * / =  ( law ha5od data bas b2ol .data )
# str   print      ( law hatba3 7aga b7otaha gowa str(..))

# INT64    ( send / publish / subscribe )  (variable).data

# SetBool  ( service / client )     (request).data --> Boolean  /
#                                (response).success --> String 
#                                (response).message --> Boolean

class My_Server(Node):
    NUM = 0
    def __init__(self):
        super().__init__("number_counter")

        self.create_subscription(Int64, "number", self.timer_call, 10)
        self.get_logger().info("subscriber is started")
        
        self.pub_num = self.create_publisher(Int64, "number_counter", 10)

        self.create_service(SetBool, "Reset_Server", self.service_call)


    def timer_call(self, msg):

        self.NUM += msg.data
        self.get_logger().info(str(self.NUM))

        pub_int = Int64()
        pub_int.data = self.NUM
        self.pub_num.publish(pub_int) 
        
        # [ publish() ] function is in file publisher.py


    #ros2 service call /Reset_Server example_interfaces/srv/SetBool "data: true"
    
    def service_call(self, rq, rsp):

        self.req = rq.data  # True / False   ( we Will Recive this object from client )

        if self.req == True: 

            self.NUM = 0

            rsp.success = True      # Boolean ( we will send this object to client )
            rsp.message = "OK_CALL"   # String  ( we will send this object to client )

        return rsp  # this return is not Totally SetBool
                    # it has only the [ Response() section ] of SetBool


def main (args=None):
    rclpy.init(args=args)
    node2 = My_Server()
    rclpy.spin(node2)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
