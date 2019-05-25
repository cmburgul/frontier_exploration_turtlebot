# frontier_exploration_turtlebot
Exploring Frontier and Mapping Autonomously on Turtlebot 

# Dependencies
* ROS (Kinetc Kame)
* Gazebo
* Rviz
* gmapping
* move_base
* actionlib

# package Depenndencies
* roscpp
* sensor_msgs
* nav_msgs
* actionlib
* actionlib_msgs
* move_base_msgs
* tf
* turtlebot packages

# Installing turtlebot packages
```
sudo apt-get install ros-kinetic-turtlebot-*
```
# Building package in catkin workspace
```
cd ~/catkin_ws/src/
git clone https://github.com/cmburgul/frontier_exploration_turtlebot.git
```
# Run the nodes individually
* Run the turtlebot_world in gazebo simulation
```
cd ~/catkin_ws/
source devel/setup.bash
roslaunch turtlebot-gazebo turtlebot_world.launch
```
* Run the Rviz to visualize the robot and sensor msgs
```
cd ~/catkin_ws/
source devel/setup.bash
roslaunch turtlebot_navigation gmapping_demo.launch 
```
* Run the package files
```
cd ~/catkin_ws/
source devel/setup.bash
rosrun frontier_exploration_turtlebot frontier_exploration_node 
```

