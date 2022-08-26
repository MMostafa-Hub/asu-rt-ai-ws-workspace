#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

# Interrupt service routine


def callback(msg: String):
    rospy.loginfo(f"{rospy.get_caller_id()} i heard {msg.data}")


def listener():
    rospy.init_node("listner", anonymous=True)
    rospy.Subscriber("chatter", String, callback)


def main():
    listener()
    rate = rospy.Rate(10)
    while True:
        rate.sleep()


if __name__ == '__main__':
    main()
