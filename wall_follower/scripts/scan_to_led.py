#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32

class ScanToLed:
    def __init__(self):
        rospy.init_node('scan_to_led_node')
        
        # 데이터 받기 (구독)
        self.sub_scan = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.sub_cmd = rospy.Subscriber('/cmd_vel', Twist, self.cmd_callback)
        
        # 아두이노로 데이터 보내기 (발행)
        self.pub = rospy.Publisher('/led_color', Int32, queue_size=10)
        
        self.min_range = 10.0
        self.linear_x = 0.0

    def scan_callback(self, msg):
        # 전방(0도) 근처의 거리 값 중 가장 작은 값 찾기
        # waffle_pi는 360도 스캔하므로 0번 인덱스가 정면입니다.
        self.min_range = msg.ranges[0]

    def cmd_callback(self, msg):
        self.linear_x = msg.linear.x
        
        color = Int32()
        
        # 판단 로직 (우선순위: 위험 > 전진/후진)
        if 0 < self.min_range < 0.5: # 50cm 이내에 벽이 있으면
            color.data = 1 # 빨강
        elif self.linear_x > 0:    # 전진 중이면
            color.data = 2 # 초록
        elif self.linear_x < 0:    # 후진 중이면
            color.data = 3 # 파랑
        else:                      # 멈춰 있으면
            color.data = 0 # 끔
            
        self.pub.publish(color)

if __name__ == '__main__':
    try:
        ScanToLed()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass