#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def callback(msg):
    temp = msg.data
    rospy.loginfo(f"수신 온도: {temp:.2f}")

    if temp >= 35.0:
        rospy.logwarn("🔥 경고! 온도가 35도 이상입니다!")

def subscriber():
    rospy.init_node('temperature_subscriber', anonymous=True)
    
    rospy.Subscriber('/temperature', Float32, callback)
    
    rospy.spin()

if __name__ == '__main__':
    subscriber()
