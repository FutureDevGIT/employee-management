## Employee Management System (Flask REST API)

A production-ready Employee Management REST API built using Flask, SQLAlchemy, and Marshmallow, demonstrating strong backend fundamentals including clean architecture, authentication, validation, pagination, and service-layer design.

### 🚀 Features

- RESTful CRUD APIs for employee management
- Token-based authentication for securing endpoints
- Input validation using Marshmallow schemas
- Pagination and filtering support for scalable data access
- Clean service layer architecture (business logic separation)
- Modular project structure using Flask Blueprints
- SQLite database using SQLAlchemy ORM
- Proper error handling and JSON responses

### 🛠️ Tech Stack

- Backend: Python, Flask
- ORM: SQLAlchemy
- Validation: Marshmallow
- Database: SQLite
- Version Control: Git & GitHub

### 📂 Project Structure
```
employee-management/
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
│
├── models/
│   └── employee.py
│
├── services/
│   └── employee_service.py
│
├── routes/
│   └── employee_routes.py
│
├── schemas/
│   └── employee_schema.py
│
├── utils/
│   └── auth.py
│
└── employees.db
```

### 🔐 Authentication

All API endpoints are protected using token-based authentication.

Header Required
```
Authorization: my-secret-token-123
```

### 📌 API Endpoints
➤ Get All Employees
```
GET /employees
```

- Query Params (Optional):
  - page – page number
  - per_page – number of records per page
  - department – filter by department
 
Example:
```
GET /employees?page=1&per_page=5&department=IT
```

➤ Get Employee by ID
```
GET /employees/<id>
```

➤ Create Employee
```
POST /employees
```

Request Body (JSON):
```
{
  "name": "Mayank",
  "email": "mayank@example.com",
  "department": "IT",
  "salary": 50000
}
```

➤ Update Employee
```
PUT /employees/<id>
```

➤ Delete Employee
```
DELETE /employees/<id>
```

### ⚙️ Setup & Run Locally
1️⃣ Clone Repository
```
git clone https://github.com/FutureDevGIT/employee-management.git
cd employee-management
```

2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # Windows
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Create Database
```
python
>>> from app import app
>>> from extensions import db
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

5️⃣ Run Application
```
python app.py
```

Server runs on:
```
http://127.0.0.1:5000
```

### 🧠 Design Highlights

- Service Layer Pattern: Keeps routes thin and logic reusable
- Blueprint Architecture: Enables modular scaling
- Validation Before Persistence: Prevents invalid data at entry
- Resolved Circular Imports: Centralized shared extensions
- Pagination & Filtering: Supports large datasets efficiently

### 📈 Future Enhancements

- JWT-based authentication
- Role-based access control
- PostgreSQL integration
- API documentation using Swagger
- Unit testing with Pytest

### 👤 Author

Mayank Raval 🤖
Python Backend Developer 💻
GitHub: https://github.com/FutureDevGIT
