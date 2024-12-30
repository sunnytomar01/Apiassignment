<<<<<<< HEAD
# Project Management Application

Getting Started
Prerequisites
Python 3.8 or later
Django 4.x or later
SQLite3 (or any preferred database)

## Virtual Environment Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

## Run the Project

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Database Migrations

1. Create migrations for changes in the database schema:
   ```bash
   python manage.py makemigrations
   ```
2. Apply the migrations to the database:
   ```bash
   python manage.py migrate
   ```

## Database Plan

### Tables and Schema

#### Users
- **Id**: Primary Key
- **Username**: String (Unique)
- **Email**: String (Unique)
- **Password**: String
- **First_name**: String
- **Last_name**: String
- **Date_joined**: DateTime

#### Projects
- **Id**: Primary Key
- **Name**: String
- **Description**: Text
- **Owner**: Foreign Key (to Users)
- **Created_at**: DateTime

#### Project Members
- **Id**: Primary Key
- **Project**: Foreign Key (to Projects)
- **User**: Foreign Key (to Users)
- **Role**: String (Admin, Member)

#### Tasks
- **Id**: Primary Key
- **Title**: String
- **Description**: Text
- **Status**: String (To Do, In Progress, Done)
- **Priority**: String (Low, Medium, High)
- **Assigned_to**: Foreign Key (to Users, nullable)
- **Project**: Foreign Key (to Projects)
- **Created_at**: DateTime
- **Due_date**: DateTime

#### Comments
- **Id**: Primary Key
- **Content**: Text
- **User**: Foreign Key (to Users)
- **Task**: Foreign Key (to Tasks)
- **Created_at**: DateTime


## Requirements

To install project dependencies:
```bash
pip install -r requirements.txt

Commands Summary
Run Project: python manage.py runserver
Create Migrations: python manage.py makemigrations
Apply Migrations: python manage.py migrate
Install Requirements: pip install -r requirements.txt
vbnet
Copy code

Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

Contact
For questions or support, contact:

Name: Sunny Tomar
Email: sunnytomar0199@gmail.com


=======
# Apitask
>>>>>>> fff5c6e0d74d29efc1a649d1990ff7a13a955e42
