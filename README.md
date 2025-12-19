# Event Management System

This is a role-based Event Management System developed using Python Flask and SQLite as part of a technical assessment.

## Features
- Login system with Admin and User roles
- Admin can add, update, cancel and remove members
- User can view reports only
- Session-based authentication
- Maintenance module controls reports
- Simple and clean user interface

## Default Login Credentials

Admin:
- Username: admin
- Password: admin123

User:
- Username: user
- Password: user123

## How to Run the Project

1. Install Python (version 3.x)

2. Install Flask:
```
pip install flask
```

3. Run the application:
```
python app.py
```

4. Open your browser and visit:
```
http://127.0.0.1:5000
```

## Database
- SQLite database file: database.db
- Tables: users, memberships, transactions

## Notes
- This project is for evaluation purposes only
- Passwords are stored in plain text for simplicity

