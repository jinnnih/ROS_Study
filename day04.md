
# Day 4 정리

## ROS Action
### ROS Action이란
```bash
시간이 오래 걸리는 작업을 처리하기 위한 통신 방식이다.
```
### Action의 특징
```bash
- 작업 진행 상태를 확인할 수 있다 (Feedback)
- 작업을 취소할 수 있다 (Cancel)
- 작업이 완료되면 결과를 받을 수 있다 (Result)
```
---
### Action 구조
```bash
Action은 다음과 같은 구조로 이루어져 있다.
Client
│
│ Goal 목표
▼
Server
│
├ Feedback (진행 상황)
│
▼
Result (완료 결과)
```
---
### Action 환경설정
## 1. package.xml 수정(아래 내용 추가)
```bash
<build_depend>actionlib</build_depend>
<build_depend>actionlib_msgs</build_depend>
<exec_depend>actionlib</exec_depend>
<exec_depend>actionlib_msgs</exec_depend>
```
## 2. CMakeLists.txt 수정(아래 내용 추가)
```bash
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  actionlib              # 추가
  actionlib_msgs         # 추가
)

add_action_files(
  FILES
  Timer.action
)

generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs         # 추가
)

catkin_package(
  CATKIN_DEPENDS actionlib_msgs   # 추가
)
```
- action 디렉토리 생성
```bash
cd ~/catkin_ws/beginner_tutorials
mkdir action
```

## TimeServer

### 1. TimerServer란
```bash
Action 서버 예제 노드, 지정된 시간 동안 타이머를 실행하는 서버
```
---

### 2. TimerServer 동작 흐름
```bash
1. TimerClient가 TimerServer에 시간 요청
2. TimerServer가 타이머 시작
3. 진행 상황을 Feedback으로 전달
4. 시간이 끝나면 Result 반환

TimerClient → Goal 요청
↓
TimerServer → 타이머 실행
↓
Feedback 전송
↓
Result 반환
```
---

## Timer.action 작성
- Timer.action
- 환경설정 적용
```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```
- 생성된 메시지 확인
```bash
rosmsg list | grep Timer
```

## timer_server.py, timer_client.py 작성 및 권한 부여 
- timer_server.py
- timer_client.py
- 권한 부여
```bash
chmod +x ~/catkin_ws/src/beginner_tutorials/scripts/timer_server.py
chmod +x ~/catkin_ws/src/beginner_tutorials/scripts/timer_client.py
```

## 실행
```bash
cd ~/catkin_ws && catkin_make
source devel/setup.bash
```
- 서버 실행(터미널1)
```bash
rosrun beginner_tutorials timer_server.py
```
- 클라이언트 실행(터미널2)
```bash
rosrun beginner_tutorials timer_client.py
```
- 취소 테스트(터미널3)
```bash
rostopic pub /timer/cancel actionlib_msgs/GoalID "{}"
```

## 오늘 배운 점
```bash
- Action은 오래 걸리는 작업을 처리하기 위한 ROS 통신 방식이다.
- Topic과 Service와는 다른 구조를 가진다.
- Action은 Goal / Feedback / Result 구조로 이루어진다.
- TimerServer는 Action Server의 동작을 이해하기 위한 예제이다.
```