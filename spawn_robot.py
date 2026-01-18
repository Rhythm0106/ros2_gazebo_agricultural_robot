import os
import subprocess
import time

ROBOT_PATH = os.path.expanduser(
    "~/agri_ws/src/farm_robot_description/urdf/farm_bot.urdf"
)

print("⏳ Waiting for Gazebo...")
time.sleep(5)

cmd = [
    "ros2", "run", "gazebo_ros", "spawn_entity.py",
    "-entity", "farm_bot",
    "-file", ROBOT_PATH,
    "-x", "-12",
    "-y", "0",
    "-z", "0.1"
]

subprocess.run(cmd)

print("✅ Robot spawned")
