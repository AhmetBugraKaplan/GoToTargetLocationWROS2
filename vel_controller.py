#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class VelControllerNode(Node): 
    def __init__(self):
        super().__init__("vel_controller_node")
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel",10)
        self.timer = self.create_timer(1, self.publist_vel)

        self.get_logger().info("Velocity Controller Node has been started !")


    def publist_vel(self):
        msg = Twist()
        linear_x = float(sys.argv[1])
        radius_ = float(sys.argv[2])
        msg.linear.x = linear_x
        msg.linear.y = 0.0
        msg.angular.z = float(linear_x/radius_) # radians: -3.14 ... +3.14
        self.publisher_.publish(msg)
        


def main (args=None):
    rclpy.init(args=args)
    node = VelControllerNode() 
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__== "__main__":
    main()