import os
import subprocess
import time

ROWS = 5
COLS = 10

ROW_SPACING = 3.0     # meters
COL_SPACING = 2.5     # meters

# Center inside 30.5 x 30.5 field
START_X = -11
START_Y = -7

MODEL_PATH = os.path.expanduser("~/.gazebo/models/plant/model.sdf")

print("Waiting for Gazebo...")
time.sleep(5)

print("Spawning plants...")

for i in range(ROWS):
    for j in range(COLS):

        x = START_X + j * COL_SPACING
        y = START_Y + i * ROW_SPACING

        name = f"plant_{i}_{j}"

        cmd = [
            "ros2", "run", "gazebo_ros", "spawn_entity.py",
            "-entity", name,
            "-file", MODEL_PATH,
            "-x", str(x),
            "-y", str(y),
            "-z", "0"
        ]

        subprocess.run(cmd)

print("Plantation completed")
