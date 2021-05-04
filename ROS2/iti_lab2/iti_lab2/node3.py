#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class My_Client(Node):

    def __init__(self):
        super().__init__("reset_client")

        self.service_client(True)    

    def service_client(self,data_msg):

        self.client = self.create_client(SetBool,"Reset_Server")

        while self.client.wait_for_service(1)==False:
            # wait_for_service()  is in file client.py      
            self.get_logger().warn("wating for server")

        self.request = SetBool.Request()
        self.request.data = data_msg                # ( we will send this object to server )

        self.future = self.client.call_async(self.request)
        # call_async() is in file (client.py)
        # future have NULL by default so won't give any error

        response_variable = SetBool.Response()
        response_variable = self.future.set_result(response_variable.message)

        self.get_logger().info(str(response_variable))

        #self.future.add_done_callback(self.future_call)
        
    #def future_call(self,future_msg):
    #    self.get_logger().info("Hello")




def main (args=None):
    rclpy.init(args=args)
    node3 = My_Client()
    #rclpy.spin(node3)
    #rclpy.spin_until_future_complete(node3,node3.future)


    rclpy.shutdown()

if __name__ == "__main__":
    main()