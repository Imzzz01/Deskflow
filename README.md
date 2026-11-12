# DeskFlow – IT Support & Asset Management System

DeskFlow is a full-stack IT support and asset management web application built with Django. The project aims to simulate a real-world IT department environment where employees can report technical issues, track support requests and manage company IT equipment.

The purpose of this project is to develop practical full-stack development skills, strengthen my understanding of backend development and build an application that demonstrates database design, authentication and CRUD functionality.

## Project Status

🚧 **Currently in development**

### Planned Features

- **User Authentication:** Secure registration, login and logout functionality.
- **Role-Based Access:** Different access levels for employees, IT support staff and administrators.
- **Ticket Management:** Create, view, update and manage IT support tickets.
- **Ticket Priorities:** Categorise tickets by priority and status.
- **Comments:** Allow users and support staff to communicate through ticket updates.
- **Asset Management:** Track company equipment and assigned devices.
- **Dashboard:** Display ticket statistics and key information.
- **Search and Filtering:** Find tickets and assets efficiently.
- **REST API:** Build API endpoints using Django REST Framework.
- **Testing:** Write tests to check application functionality.

## Project Structure

```text
Deskflow/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   └── views.py
│
├── assets/
│
├── tickets/
│
├── dashboard/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Deskflow
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django djangorestframework "psycopg[binary]" python-dotenv
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Learning Objectives

Through building DeskFlow, I aim to gain practical experience in:

- Designing relational databases and Django models.
- Understanding relationships between database tables.
- Implementing authentication and permissions.
- Building CRUD functionality.
- Developing RESTful APIs.
- Writing and debugging Python code.
- Testing and deploying a full-stack application.
- Using Git and GitHub throughout the development lifecycle.

## Author

Developed as a personal portfolio project to demonstrate my ongoing learning and development in Python, Django and full-stack web development.
