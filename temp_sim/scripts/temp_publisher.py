#!/usr/bin/env python3

import rospy
import random
from std_msgs.msg import Float32

def publisher():
    rospy.init_node('temperature_publisher', anonymous=True)
    
    pub = rospy.Publisher('/temperature', Float32, queue_size=10)
    
    rate = rospy.Rate(1)  # 1Hz (1초에 1번)

    while not rospy.is_shutdown():
        temp = random.uniform(20.0, 40.0)
        
        rospy.loginfo(f"현재 온도: {temp:.2f}")
        pub.publish(temp)
        
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
