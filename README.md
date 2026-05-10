# Robotics Motion Planning & Kinematics (Task 2)

This repository contains Python-based implementations of various robotic drive systems and kinematics models. The project focuses on writing comments on motion simulation for different steering geometries and integrated library components for mobile robotics.

## 🚀 Featured Kinematics Models

* **Ackermann Steering:** Implementation of the Ackermann geometry for car-like vehicles, handling inner and outer wheel angles for slip-free turning.
* **Mecanum Drive:** Kinematics for omnidirectional movement, allowing for translation in any direction and rotation simultaneously.
* **Two-Wheel Differential Drive:** Classic differential drive model for simple mobile robots.

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `motion_ackermann_demo.py` | Demo script for car-like steering geometry. |
| `motion_mecanum_demo.py` | Script for 4-wheel omnidirectional motion. |
| `motion_two_wheel_demo.py` | Differential drive motion simulation. |
| `live_ackermann_session.py` | Real-time calculation/visualization session for Ackermann steering. |
| `*.png` | Visualizations and output plots for the motion demos. |

## 🛠️ Requirements & Installation

This project utilizes the **Aurora-Mobile-Robotics-Library** for core calculations.

1. **Clone the repository:**
   ```bash
   git clone git@github.com:Joajibola/core2-task2.git
   cd "core 2 task 2"
