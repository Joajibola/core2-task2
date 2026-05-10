#!/usr/bin/env python3
"""Two-wheel (v, ω) model: forward, turn, backward, drive_to_pose with dotted tire traces."""

from __future__ import annotations

import math
import os #prpvides tools for writing to the file system

#Library for ploting the graph
import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

p0 = amr.pose(0.0, 0.0, 0.0) #Defines the starting point (X=0, Y=0, facing north (CCW) )
params = amr.TwoWheelParams(track_width=0.45, max_linear_speed=1.2, max_angular_speed=1.5) #Sets some key parameters like the distance between the two wheels, top speed going forward, top spinning speed
session = amr.MotionSession.create(p0, amr.KinematicsModel.TWO_WHEEL, dt=0.015, unicycle=params) #initialise the simulation using the two-wheel model

#The entire motion command
session.forward(1.5, 0.6)
session.turn_right(math.pi / 2, 1.0)
session.forward(1.0, 0.6)
session.backward(0.5, 0.4)
goal = amr.pose(0.5, 2.0, math.pi / 6) #This defines the specific target
session.drive_to_pose(goal, linear_speed=0.7, angular_speed=1.2, position_tol=0.08, angle_tol=0.08) # This line tell it to drive to the goal pose specified above

# This remaining blocks are for the visualisation
fig, ax = plt.subplots(figsize=(8, 8)) # size of the plot 8 by 8

#plots the robot movement history
amr.plot_motion(session, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "motion_two_wheel_demo.png"), dpi=150) # it saves the plot to "motion_two_wheel_demo.png"
print("Saved motion_two_wheel_demo.png, final pose:", session.pose) # output message in the terminal
