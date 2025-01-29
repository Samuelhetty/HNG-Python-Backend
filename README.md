# Basic Info Project

## Project Overview
The **Basic Info Project** is a Django web application designed to store and display basic information. This project leverages Django's admin interface, migrations, and templates.

## Table of Contents
1. [Technologies](#technologies)
2. [Setup](#setup)
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

### 2. Install Dependencies

pip install -r requirements.txt

## Running Locally

### 1. Apply Migrations
Make sure your database is set up:

python manage.py migrate

### 2. Run the Development Server

python manage.py runserver

## Deploy
Follow the platform's guide to create a new project. For example, on Render:

_Create a new web service.
_Connect your repository.
_Set up environment variables (e.g., DJANGO_SECRET_KEY, DATABASE_URL).
_Configure the Root Directory (if needed).

## Start Deployment
Trigger the deployment, and once successful, your app will be live.

### License
This project is licensed under the MIT License – see the LICENSE file for details.