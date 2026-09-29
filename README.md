# Employee Management System — Day 15 and DAy 14

 **Project Nexelis | Intern-to-Engineer Bootcamp**

A backend-focused Employee Management System developed as the Day 15 mini project to integrate the concepts learned from Python fundamentals through REST API development, FastAPI, PostgreSQL, validation, and API quality.


## 👨‍💻 Author

**Shivam Jha**  
B.Tech CSE Student  
Project Nexelis — Intern-to-Engineer Bootcamp



## 📌 Project Overview

The Employee Management System is a RESTful backend application designed to manage employees and departments.

The project brings together the major engineering concepts covered during Days 6–14:

- Python Programming
- Object-Oriented Programming
- PostgreSQL
- Relational Database Design
- SQL
- REST APIs
- FastAPI
- Pydantic Validation
- Error Handling
- Pagination
- Search
- Filtering
- Sorting
- Logging
- Git & GitHub

The objective is not only to make the API functional, but to structure it like a maintainable backend application.



## 🎯 Project Objective

The system provides APIs for managing:

### Employees

- Create employee
- View all employees
- View employee by ID
- Search employees
- Update employee
- Partially update employee
- Delete employee

### Departments

- Create department
- View departments
- Update department
- Delete department



## 🏗️ System Architecture

                    Client
                      │
                      ▼
                REST Request
                      │
                      ▼
                  FastAPI
                      │
                      ▼
              Request Validation
                  (Pydantic)
                      │
                      ▼
                API / Router
                      │
                      ▼
             Business / Service
                   Layer
                      │
                      ▼
              Repository Layer
                      │
                      ▼
                SQLAlchemy
                      │
                      ▼
                 PostgreSQL