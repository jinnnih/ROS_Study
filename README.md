# ROS development
- Ubuntu 20.04
- ROS noetic

# ROS install
1. source list
```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

2. Setup your sources.list
```bash
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

3. Installation
```bash
sudo apt update
sudo apt install ros-noetic-desktop-full
```

4. Environment setup
```bash
source /opt/ros/noetic/setup.bash
```

5. Create a ROS Workspace
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
echo $ROS_PACKAGE_PATH
```

# ROS packages
1. Building Packages
```bash
source /opt/ros/kinetic/setup.bash
catkin_make [make_targets] [-DCMAKE_VARIABLES=...]
mkdir build
cd build
cmake ..
make
make install 
catkin_make
catkin_make install
```

2. Building Your Package
```bash
cd ~/catkin_ws/
ls src
catkin_make
ls
```

# Understanding ROS Nodes
1. Prerequisites
```bash
sudo apt-get install ros-noetic-ros-tutorials
```
2. roscore
```bash
roscore
sudo chown -R <your_username> ~/.ros
```
3. Using rosnode
```bash
rosnode list
rosnode info /rosout
```
4. Using rosrun
```bash
rosrun turtlesim turtlesim_node
```
In a new terminal:
```bash
rosnode list
rosnode ping my_turtle
```

# /turtle1/pose 관찰 (ROS Topics)
1. Setup
```bash
roscore  # 1번만 실행
rosrun turtlesim turtlesim_node # 새 터미널을 열어 터틀심 사용
rosrun turtlesim turtle_teleop_key # 키보드로 터틀심 제어하는 명령어
# 거북이가 움직이지 않는다면 turtle_teleop_key의 터미널 창에서 입력한 것이 맞는지 확인
## /turtle1/pose 필드 분석
- x: 거북이의 X 좌표. 앞으로 이동하면 값이 증가한다

- y: 거북이의 Y 좌표. 위로 이동하면 값이 증가한다

- theta: 거북이의 방향 좌회전하면 값이 증가, 우회전하면 감소한다

- linear_velocity: 현재 직진 속도. 방향키 위를 누르면 2.0이 된다

- angular_velocity: 현재 회전 속도. 방향키 좌를 누르면 2.0이 된다

```

2. ROS Topics
- Using rqt_graph 
```bash
sudo apt-get install ros-noetic-rqt #rqt그래프 패키지 설치
sudo apt-get install ros-noetic-rqt-common-plugins
# In a new terminal: (안해도 된다.)
rosrun rqt_graph rqt_graph # 그래프 실행
```

- Introducing rostopic
```bash
rostopic -h  # 도움말 옵션 / 하위 명령어 확인
rostopic 
```

- Using rostopic echo
```bash
rostopic echo [topic]
rostopic echo /turtle1/cmd_vel
rostopic echo /turtle1/command_velocity
# 해당 토픽에 데이터가 게시되지 않으므로 아무것도 안 나옴. 화살표 키를 눌러 turtle_teleop_key가 데이터를 게시하고 거북이가 움직이지 않으면 turtle_teleop_key 터미널을 다시 선택

```

- Using rostopic list
```bash
rostopic list -h #현재 구독 중이거나 게시 중인 모든 토픽 목록의 도움말
rostopic list -v
```
