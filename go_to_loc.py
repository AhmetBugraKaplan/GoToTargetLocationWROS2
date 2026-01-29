#!/usr/bin/env python3

import rclpy
import math
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class GoToLocationNode(Node): 
    def __init__(self):
        super().__init__("go_to_loc_node")
        self.pose_treshold_linear = 0.3
        self.pose_treshold_angular = 0.03

        self.targets = [
            (2.0, 2.0),
            (8.0, 2.0),
            (8.0, 8.0),
            (2.0, 8.0)
        ]
        self.current_target_index = 0

        self.publiser_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.callback_turtle_pose, 10)
        self.timer = self.create_timer(0.1, self.turtle_controller)

        self.get_logger().info("Go To Location Node has been started !")

    
    def turtle_controller(self):
        if not hasattr(self, "pose_"):
            return

        if self.current_target_index >= len(self.targets):
            return

        target_x, target_y = self.targets[self.current_target_index]

        msg = Twist()
        dist_x = target_x - self.pose_.x
        dist_y = target_y - self.pose_.y

        distance = math.sqrt(dist_x**2 + dist_y**2)
        target_theta = math.atan2(dist_y, dist_x)

        if abs(target_theta - self.pose_.theta) > self.pose_treshold_angular:
            msg.angular.z = target_theta - self.pose_.theta
        else:
            if distance >= self.pose_treshold_linear:
                msg.linear.x = distance
            else:
                msg.linear.x = 0.0
                self.current_target_index += 1

        self.publiser_.publish(msg)


    def callback_turtle_pose(self, msg):
        self.pose_ = msg


def main(args=None):
    rclpy.init(args=args)
    node = GoToLocationNode() 
    rclpy.spin(node)
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()
