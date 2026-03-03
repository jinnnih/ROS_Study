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
sudo apt install curl # if you haven't already installed curl
```
```bash
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

3. Installation
```bash
sudo apt update
```
```bash
sudo apt install ros-noetic-desktop-full
```

4. Environment setup
```bash
source /opt/ros/noetic/setup.bash
```

5. Create a ROS Workspace
```bash
mkdir -p ~/catkin_ws/src
```
```bash
cd ~/catkin_ws/
```
```bash
catkin_make
```
```bash
source devel/setup.bash
```
```bash
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