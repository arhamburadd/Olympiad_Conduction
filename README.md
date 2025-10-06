#  Olympiad Conduction System

A full-fledged **Olympiad management system** built with **Python** and **MySQL**, featuring an interactive **Tkinter GUI** for registration, subject allocation, marks entry, grading, and automated result generation.

---

## Overview

This system streamlines the entire Olympiad process — from **student registration** to **final results** — providing a simple graphical interface for students and administrators.

### Core Functionalities
- Student Registration with subject selection
- Host/Admin panel for marks entry
- Automatic grading and pass/fail evaluation
- Result display with **All India Rank (AIR)** and **State Rank**
- Secure MySQL database integration
- GUI-based workflow using Tkinter



##  Project Structure
```
Olympiad-Conduction-System/
│
├── README.md
├── requirements.txt
├── LICENSE
│
├── src/
│   ├── main.py              # Core application – controls flow between modules
│   ├── allocation.py        # Handles marks entry and host interface
│   ├── result.py            # Displays student results and ranks
│   ├── __init__.py
│
├── database/
│   ├── db_config.py         # MySQL connection setup
│   ├── schema.sql           # Database and table creation script
│
├── assets/
│   ├── screenshots/         # GUI screenshots (optional)
│   └── icons/               # App icons or logo (optional)
│
└── docs/
    └── user_guide.md        # Instructions for users/admins

```

##  Setup & Installation

### Prerequisites
- Python 3.x  
- MySQL Server  

### Install dependencies
```bash
pip install mysql-connector-python
