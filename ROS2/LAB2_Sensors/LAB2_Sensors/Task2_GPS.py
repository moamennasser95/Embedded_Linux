#!/usr/bin/env python3
import rclpy
import csv
import numpy as np
from rclpy.node import Node
from math import sin, cos, pi
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Quaternion
from tf2_ros import TransformBroadcaster, TransformStamped
from sensor_msgs.msg import Imu
from example_interfaces.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from sensor_msgs.msg import NavSatFix


#TODO Import needed messages

class Task2_GPS(Node):
    def __init__(self):
        super().__init__("Task2_GPS") 
        self.csv_file_path = "GGA_GST.csv"
        self.lines = []
        with open(self.csv_file_path, newline='\n') as csvfile:       
          self.readCSV = csv.reader(csvfile, delimiter = ',')
          for row in self.readCSV:
              self.lines.append(row)

        self.count = 1 #Skip header
        
        ## create timer_call with the required frequency & publisher
        self.i_will_publish_now = self.create_publisher(NavSatFix,"fix",10)
        self.create_timer(1/3,self.timer_call)


    def timer_call(self):
        row = self.lines[self.count]
        self.count +=1
        if (self.count >= len(self.lines)): # repeat csv file continously
            self.count = 0

        ## get The following values from csv
        latitude_value = row[2]
        latitude_direction = row[3]
        longitude_value = row[4]
        longitude_direction = row[5]
        altitude_value = row[9]
        hdop = row[8]
        self.lat_std_dev = row[21]
        self.lon_std_dev = row[22]
        self.alt_std_dev = row[23]

        # The following functions convert the string data in degrees/minutes to float data in degrees as ROS message requires.        
        latitude = self.convert_latitude(latitude_value, latitude_direction)
        longitude = self.convert_longitude(longitude_value, longitude_direction)
        altitude = self.safe_float(altitude_value)

        ## Fill the gps message and publish
        current_fix = NavSatFix()

        current_fix.header.stamp = self.get_clock().now().to_msg()
        current_fix.header.frame_id = "gps_link"

        current_fix.latitude = latitude

        current_fix.longitude = longitude

        current_fix.altitude = altitude

        current_fix.position_covariance[0] = str((hdop * self.lon_std_dev) ** 2)
        current_fix.position_covariance[4] = (hdop * self.lat_std_dev) ** 2
        current_fix.position_covariance[8] = (2 * hdop * self.alt_std_dev) ** 2

        self.i_will_publish_now.publish(current_fix)


    def convert_latitude(self, field_lat, lat_direction):
        latitude = self.safe_float(field_lat[0:2]) + self.safe_float(field_lat[2:]) / 60.0
        if lat_direction == 'S':
            latitude = -latitude
        return latitude

    def convert_longitude(self, field_long, long_direction):
        longitude = self.safe_float(field_long[0:2]) + self.safe_float(field_long[2:]) / 60.0 
        if long_direction == 'W':
            longitude = -longitude
        return longitude

    def safe_float(self, field):
        try:
            return float(field)
        except ValueError:
            return float('NaN')

def main (args=None):
    rclpy.init(args=args)
    node = Task2_GPS()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()