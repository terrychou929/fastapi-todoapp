# Todo App - FastAPI & SQLAlchemy

## Project Overview

This project is a simple **Todo List Application** built with **FastAPI**, **SQLAlchemy**, and **Jinja2** for the backend. It allows users to create, read, update, and delete (CRUD) their todo items. The application interacts with a **PostgreSQL** database for persistent storage of todos.

### Features:
- Create new todos.
- View all todos.
- Update existing todos.
- Delete todos.
- The app uses FastAPI to handle the backend logic and SQLAlchemy for ORM-based interaction with the database.
- Jinja2 is used for rendering the frontend templates.

---

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLAlchemy**: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Jinja2**: A templating engine for Python, used to render HTML templates on the frontend.
- **PostgreSQL**: A powerful, open-source relational database management system (RDBMS).
- **Docker**: To containerize the application and make it easier to deploy and run consistently across different environments.
- **Docker Compose**: A tool for defining and running multi-container Docker applications, making it easy to run FastAPI and PostgreSQL together.

---

## Installation and Setup

### Prerequisites

1. **Docker** and **Docker Compose** must be installed on your machine.
2. **Python** 3.7+ (only required if you're not using Docker to run the app).
3. **PostgreSQL** database (this is handled by Docker Compose in this project).

### Steps to Install and Run the Application

#### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/fastapi-todoapp.git
cd fastapi-todoapp
``` 

#### 2. Set up the environment variables:
Make sure your .env file is correctly configured to connect to the PostgreSQL database.

#### 3. Using Docker (Recommended):
To run the app in a containerized environment using Docker, follow these steps:

``` shell
docker-compose build
docker-compose up
```

This will start the FastAPI application and the PostgreSQL database in separate containers. The FastAPI app will be accessible at http://localhost:8000.