Child Health Monitoring API

A Django REST Framework API that helps track children’s health information, including personal details, health records, and vaccination history.
This project is being developed as part of my Backend Engineering Capstone Project.

📖 Project Overview

Many children in low-income communities lack access to proper health tracking. Parents and healthcare providers often struggle with keeping up-to-date records, leading to missed vaccinations and unnoticed growth issues.

This API aims to provide:

A way to register children and link them to guardians

Health records (height, weight, notes) for growth monitoring

Vaccination tracking with status updates

A base system that can later integrate with mobile or web apps

Capstone Progress
Part 1 – Idea & Planning

Selected project: Child Health Monitoring API
Defined the problem and proposed solution
Outlined key features and user stories

Part 2 – Design

Created an ERD (Entity Relationship Diagram)
Planned the database models (Child, HealthRecord, Vaccination)
Designed REST API endpoints

Part 3 – Start Building

Set up Django project and health app
Installed and configured Django REST Framework
Built initial models, serializers, and viewsets
Implemented CRUD endpoints with DRF routers
Tested endpoints using Postman and Django’s browsable API




Tech Stack

Backend: Django, Django REST Framework
Database: SQLite (dev), PostgreSQL (prod-ready)
Tools: Postman, GitHub, Render

📂 Project Structure
child_health_monitoring_api/
    child_health_api/
    ├── child_health_api/        # Project settings
    ├── health/                  # App: models, serializers, views, urls
    ├── manage.py
    ├── requirements.txt
    └── README.md
