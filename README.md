
# ROS2 Gazebo Agricultural Robot Simulation

This repository contains a ROS2 + Gazebo simulation of an agricultural field environment with an autonomous ground robot.  
The project focuses on simulation-first development for agricultural robotics applications.

## Features
- Custom agricultural field world (30.5m x 30.5m soil terrain)
- Plant models arranged in crop rows
- ROS2-integrated Gazebo simulation
- Scalable robot model using URDF/Xacro
- Modular structure for future sensor integration

## Technologies Used
- ROS2 Humble
- Gazebo Classic
- URDF / Xacro
- Python
- Linux

## Current Status
- Environment and plant models completed
- Robot model integrated and visible in Gazebo
- Simulation launch pipeline established
- Sensor integration and navigation: **In progress**

## How to Run
```bash
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
ros2 launch agri_robot_simulation gazebo.launch.py
