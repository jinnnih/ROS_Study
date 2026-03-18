#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def pose_callback(msg):
    x = msg.x
    y = msg.y

    rospy.loginfo("Current position -> x: %.2f, y: %.2f", x, y)

    if x <= 1.0 or x >= 10.0 or y <= 1.0 or y >= 10.0:
        rospy.logwarn("⚠️ WARNING: Turtle is near the wall!")

def monitor():
    rospy.init_node('turtle_position_monitor', anonymous=True)

    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    rospy.spin()

if __name__ == '__main__':
    monitor()
