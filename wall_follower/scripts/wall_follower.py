#!/usr/bin/env python3
import rospy
import math
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

# ===== 파라미터 =====
LINEAR_SPEED = 0.15
ANGULAR_SPEED = 1.0  # 너무 빠르면 진동이 심해지니 1.0 정도로 조절해보세요
DESIRED_DISTANCE = 0.5

class WallFollowerPID:
    def __init__(self):
        rospy.init_node('wall_follower_pid')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

        # PID 게인 - 속도를 올렸다면 kd를 조금 더 높여야 안정적입니다.
        self.kp = 0.7 
        self.ki = 0.0
        self.kd = 0.1  

        self.integral = 0.0
        self.prev_error = 0.0
        self.dt = 0.1
        self.rate = rospy.Rate(10)

    def get_range(self, scan, angle):
        if 1.40 <= angle <= 1.75: # 구멍(문) 필터
            return 10.0
        index = int((angle - scan.angle_min) / scan.angle_increment)
        index = max(0, min(index, len(scan.ranges) - 1))
        distance = scan.ranges[index]
        if math.isnan(distance) or math.isinf(distance) or distance == 0:
            distance = 10.0
        return distance

    def get_error(self, scan, desired_distance):
        theta = math.radians(45)
        a = self.get_range(scan, math.radians(45))
        b = self.get_range(scan, math.radians(90))

        if b >= 2.0 or a >= 10.0:
            return self.prev_error 

        alpha = math.atan2(a * math.cos(theta) - b, a * math.sin(theta))
        current_wall_dist = b * math.cos(alpha)
        
        # [수정] 왼쪽 벽 기준: 벽이 가까워지면(dist < desired) 결과가 마이너스
        # 마이너스 결과 -> 우회전(-)이 되도록 설정
        return current_wall_dist - desired_distance

    def pid_control(self, error):
        p_term = self.kp * error
        self.integral += error * self.dt
        i_term = self.ki * self.integral
        d_term = self.kd * (error - self.prev_error) / self.dt
        
        angular_z = p_term + i_term + d_term
        self.prev_error = error

        twist = Twist()
        twist.linear.x = LINEAR_SPEED
        twist.angular.z = angular_z
        self.pub.publish(twist)

    def scan_callback(self, scan):
        front = self.get_range(scan, 0.0)
        error = self.get_error(scan, DESIRED_DISTANCE)

        if front < 0.6: # 충돌 방지를 위해 범위를 0.6으로 약간 넓힘
            twist = Twist()
            # [수정] 왼쪽 벽을 따라가려면 정면 장애물 시 '우회전' 해야 함
            twist.angular.z = -ANGULAR_SPEED 
            self.pub.publish(twist)
            rospy.loginfo("장애물 감지 - 우회전 회피")
        else:
            self.pid_control(error)

if __name__ == '__main__':
    try:
        wf = WallFollowerPID()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass