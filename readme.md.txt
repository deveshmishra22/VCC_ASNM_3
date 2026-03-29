# Cloud Auto-Scaling Simulation Project

## Objective
This project is for demonstration of simple auto-scaling mechanism where a local VM python program monitors its CPU usage and offloads tasks to a cloud VM when CPU utilization exceeds a threshold (75%).

---

## Architecture Overview

Local System (WSL / VM)  
- Monitors CPU usage  
- Decision Engine  
- If CPU < 75% → Execute locally  
- If CPU ≥ 75% → Offload task to Cloud VM  

Cloud VM (GCP)  
- Flask API processes heavy tasks  
- Returns result to local system  

---

## Technologies Used
- Python
- Flask (Cloud API)
- psutil (CPU monitoring)
- requests (HTTP communication)
- Google Cloud Platform (GCP VM)

---

## Project Structure
Assignment3/
│
- local/
│ - monitor.py
│ - requirements.txt
│
 - cloud/
│ - app.py
│ - requirements.txt
│
 - docs/
│  - report file
│  - architecture file
|  - Video file
│
- README.md
- .gitignore
