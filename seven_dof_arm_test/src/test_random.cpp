#include <moveit/move_group_interface/move_group_interface.h>


int main(int argc, char **argv)
{
  ros::init(argc, argv, "move_group_interface_demo", ros::init_options::AnonymousName);
  // start a ROS spinning thread
  ros::AsyncSpinner spinner(1);
  spinner.start();
  // this connecs to a running instance of the move_group node
	moveit::planning_interface::MoveGroupInterface group("arm");
  // specify that our target will be a random one
  // group.setRan최종 정리
demo.launch는 [ Gazebo(물리 엔진) ] 없이 RViz만으로 모션 플래닝을 시뮬레이션한다.

Gazebo와 연동하면 [ 물리(Physics) ] 시뮬레이션이 적용되어 로봇이 실제처럼 움직인다.

두 경우 모두 내부에서는 [ move_group ] 노드가 IK 계산 → 경로 계획 → 실행을 수행한다.domTarget();
  // plan the motion and then move the group to the sampled target 
  group.move();
  ros::waitForShutdown();
}
