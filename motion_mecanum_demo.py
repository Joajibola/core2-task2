#!/usr/bin/env python3
"""Mecanum X-config: omnidirectional motion and four wheel traces (FL, FR, RL, RR)."""

from __future__ import annotations

import math # Library for assessing the math operations like "pi"
import os 

import matplotlib.pyplot as plt # Library used for plottign graphs

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

# Mecanum wheels are defined by the distance from the center to the rollers.
# half_length_y: vertical distance from center to front/rear axle.
# half_width_x: horizontal distance from center to left/right wheel
params = amr.MecanumParams(half_length_y=0.28, half_width_x=0.22, max_wheel_speed=2.5)
session = amr.MotionSession.create(
    amr.pose(0.0, 0.0, 0.0), #Defines the starting point (X=0, Y=0, facing north (CCW) )
    amr.KinematicsModel.MECANUM,
    dt=0.015,
    mecanum=params,
)

#The motions
session.forward(1.0, 0.7) # Drive straight forward for 1.0 meter at 0.7 m/s
session.strafe_right(0.8, 0.6) # Strafe (slide) directly to the right for 0.8 meters at 0.6 m/s.
session.turn_left(math.pi / 3, 1.0) # Rotate counter-clockwise (left) by 60 degrees (pi/3) at 1.0 rad/s
session.mecanum_drive_wheels(0.5, -0.2, 0.0, 0.8, duration=1.0)

goal = amr.pose(1.5, 0.5, math.pi / 6) #This defines the specific target
session.drive_to_pose(goal, linear_speed=0.6, angular_speed=1.0, position_tol=0.1, angle_tol=0.12)# This line tell it to drive to the goal pose specified above at a specific linear and angular speed

#plots the robot movement history

fig, ax = plt.subplots(figsize=(8, 8))
amr.plot_motion(session, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "motion_mecanum_demo.png"), dpi=150)
print("Saved motion_mecanum_demo.png") # Prints this to terminal
