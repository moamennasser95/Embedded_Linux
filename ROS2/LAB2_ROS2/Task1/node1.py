#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from example_interfaces.msg import Int64

class My_Publish(Node):

    def __init__(self):
        super().__init__("Int_publisher")

        self.get_logger().info("Pub_Node_Started_ok")
        self.i_will_publish_now = self.create_publisher(Int64,"number",10) # Will Create the topic
        self.create_timer(1/1,self.timer_call)
        self.counter = 5

    def timer_call(self):
        interger = Int64()
        interger.data = self.counter
        self.get_logger().info(str(self.counter))
        self.i_will_publish_now.publish(interger)

def main (args=None):

    rclpy.init(args=args)
    node1 = My_Publish()
    rclpy.spin(node1)
    rclpy.shutdown()


if __name__ == "__main__":
    main()





#self.msg_str = String()
#self.msg_str.data = "{}".format(self.counter)
#self.i_will_publish_now.publish(str(self.counter))
#from example_interfaces.msg import Int64
#from example_interfaces.msg import Bool
#from example_interfaces.srv import AddTwoInts