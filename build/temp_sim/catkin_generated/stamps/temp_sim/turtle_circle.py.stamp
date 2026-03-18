#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_circle():
    rospy.init_node('turtle_circle_publisher', anonymous=True)

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)  # 10Hz

    while not rospy.is_shutdown():
        msg = Twist()

        msg.linear.x = 1.0      # 직진 속도
        msg.angular.z = 2.0     # 회전 속도

        pub.publish(msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_circle()
    except rospy.ROSInterruptException:
        pass
