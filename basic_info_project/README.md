# Basic Info Project

## Project Overview
The **Basic Info Project** is a Django web application designed to store and display basic information. This project leverages Django's admin interface, migrations, and templates.

## Table of Contents
1. [Technologies](#technologies)
2. [Setup](#setup)
3. [API Documentation](#api-documentation)
3. [Running Locally](#running-locally)
4. [Deploying to Production](#deploying-to-production)

## Technologies
- **Django** (v5.1.5) – Python web framework
- **SQLite** – Database
- **Gunicorn** – WSGI HTTP Server for UNIX
- **Render**  – Deployment platforms

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/samuelhetty/HNG-Python-Backend.git
cd basic_info_project 
```

### 2. Install Dependencies

pip install -r requirements.txt

# **API Documentation **

## Base URL
The base URL for all API requests is: https://hng-python-backend.onrender.com

### GET `/api/basic_info_app/`

#### Description:
Fetches a list of all basic information records stored in the database.

#### Request:
- **Method**: GET
- **URL**: `/api/basic_info_app/`

#### Response:
- **Status**: 200 OK
- **Body**: JSON array containing all records.
```json
[
  {
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "<https://github.com/yourusername/your-repo>"
 }
]
```

## Running Locally

### 1. Apply Migrations
Make sure your database is set up:

python manage.py migrate

### 2. Run the Development Server

python manage.py runserver

### Example Usage

- curl -X GET http://127.0.0.1:8000/api/basic_info_app/

## Deploy
Follow the platform's guide to create a new project. For example, on Render:

- Create a new web service.
- Connect your repository.
- Set up environment variables (e.g., DJANGO_SECRET_KEY, DATABASE_URL).
- Configure the Root Directory (if needed).

## Start Deployment
Trigger the deployment, and once successful, your app will be live.

### License
This project is licensed under the MIT License – see the LICENSE file for details.

### Programming language - [PYTHON](https://hng.tech/hire/python-developers)



## Authors

- [Henrietta Onoge](https://github.com/Samuelhetty)