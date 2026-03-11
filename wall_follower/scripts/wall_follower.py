#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

# ===== 파라미터 =====
DIST_THRESHOLD = 0.8   # 벽까지 이 거리 이내면 "가깝다"고 판단 (m)
LINEAR_SPEED = 0.4    # 전진 속도 (m/s)
ANGULAR_SPEED = 0.3    # 회전 속도 (rad/s)

class WallFollower:
    def __init__(self):
        rospy.init_node('wall_follower')
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        self.regions = {}
        self.state = 'find_wall'
        self.rate = rospy.Rate(10)

    def scan_callback(self, scan):
        # LaserScan 데이터를 5개 영역으로 분할
        self.regions = {
            'right':       min(min(scan.ranges[0:144]),   10),
            'front_right': min(min(scan.ranges[144:288]), 10),
            'front':       min(min(scan.ranges[288:432]), 10),
            'front_left':  min(min(scan.ranges[432:576]), 10),
            'left':        min(min(scan.ranges[576:720]), 10),
        }

    def decide_state(self):
        r = self.regions
        if not r:
            return

        d = DIST_THRESHOLD

        # [기존 우측 벽 기준 판단 로직]
        # if r['front'] > d and r['front_right'] > d and r['right'] > d:
        #     self.state = 'find_wall'
        # elif r['front'] < d:
        #     self.state = 'turn_left'
        # else:
        #     self.state = 'follow_wall'

        # [수정된 좌측 벽 기준 판단 로직]
        if r['front'] > d and r['front_left'] > d and r['left'] > d:
            self.state = 'find_wall'
        elif r['front'] < d:
            self.state = 'turn_right'  # 전방 장애물 발견 시 우회전
        else:
            self.state = 'follow_wall'
        

    def act(self):
        twist = Twist()

        if self.state == 'find_wall':
            # 벽을 찾을 때까지 전진 + 약간 좌회전 (왼쪽 벽을 향함)
            twist.linear.x = LINEAR_SPEED
            twist.angular.z = ANGULAR_SPEED * 0.5  # 양수(+)는 좌회전
            
        elif self.state == 'turn_right':
            # 전방에 벽이 감지되면 오른쪽으로 회전하여 회피
            twist.angular.z = -ANGULAR_SPEED       # 음수(-)는 우회전
            
        elif self.state == 'follow_wall':
            # 왼쪽에 벽이 있는 상태로 판단되면 직진
            twist.linear.x = LINEAR_SPEED

        self.pub.publish(twist)

    def run(self):
        rospy.loginfo("Wall Follower 시작 (좌측 벽 추종 모드)")
        while not rospy.is_shutdown():
            self.decide_state()
            self.act()
            if self.regions:
                # 디버깅 편의를 위해 로그 출력을 좌측 기준으로 변경했습니다.
                rospy.loginfo("상태: %-12s | 좌측: %.2f | 좌전방: %.2f | 전방: %.2f",
                              self.state,
                              self.regions['left'],
                              self.regions['front_left'],
                              self.regions['front'])
            self.rate.sleep()

if __name__ == '__main__':
    try:
        wf = WallFollower()
        wf.run()
    except rospy.ROSInterruptException:
        pass