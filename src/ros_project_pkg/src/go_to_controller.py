#!/usr/bin/env python3
import operator
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import numpy as np
import math

param = rospy.get_param("/consts")
param["beta"] = .1
param["phi"] = .1


def input_goals():
    return tuple(map(int, input("input goals: ").split(" ")))


def control(pose: Pose):
    d_x = goal_x - pose.x
    d_y = goal_y - pose.y
    msg_vel.linear.x = param["beta"] * math.sqrt(d_x**2+d_y**2)
    msg_vel.angular.z = param["phi"] * (-pose.theta + np.arctan2(d_y, d_x))
    return d_x, d_y


def callback(pose: Pose):
    global goal_x, goal_y

    d_x, d_y = control(pose)
    if abs(d_y) < 1 and abs(d_x) < 1:
        rospy.loginfo(f"Arrived to goal, {pose.x, pose.y}")
        goal_x, goal_y = input_goals()
    else:
        pub.publish(msg_vel)


goal_x, goal_y = input_goals()
msg_vel = Twist()

rospy.init_node("go_to_controller_node")
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
sub = rospy.Subscriber("/turtle1/pose", Pose, callback, queue_size=10)
rate = rospy.Rate(1)
rate.sleep()

rospy.spin()
