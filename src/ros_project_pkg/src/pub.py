#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('duck')
pub = rospy.Publisher("chatter", String)


msg = String()
msg.data = "Quack"

while not rospy.is_shutdown():
    pub.publish(msg)
    rospy.sleep(1)

