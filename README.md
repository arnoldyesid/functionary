# 📦 Functionary

![Docker](https://img.shields.io/badge/Docker-v24.0.2-blue) ![Make](https://img.shields.io/badge/Makefile-Ready-green)

Functionary is an e-commerce backend service that allows users to register, log in, create orders, and check order statuses. This project leverages Docker for containerization and `make` for managing build and service commands.

## 🚀 Features

- User registration and authentication
- Order creation and management
- Endpoint for checking past due orders
- Easy-to-deploy Docker environment

## 🛠 Requirements

Before running the service, ensure you have the following installed:

- **Docker** (version 24.0.2 or higher)
- **Make**

## 🏃‍♂️ Quick Start

Follow these steps to get the service up and running:

1. **Navigate to the project directory:**
   ```bash
   cd E-commer-project-main
   make build
   make test
   make check_past_due_orders

📝 Register
Endpoint: POST http://{host}:8001/api/user/register
Body:
{
  "name": "Arnold", 
  "email": "ar12no21ldw.blandon3@gmail.com",
  "password": "12345678"
}

Response:
{
  "name": "TEST",
  "email": "test@gmail.com"
}

🔑 Login
Endpoint: POST http://{host}:8001/api/user/login
Body:
{
  "email": "user@gmail.com",
  "password": "12345678"
}
Response:
{
  "access": "eyJ0e.."
}

🛒 Create Order
Authorization: Bearer token required
Endpoint: POST http://{host}:8001/api/order/new
Body:
{
  "sku": "2922511",
  "name": "cellphone",
  "price": 2323.21,
  "delivery_date": "01-01-2024"
}

Response:
{
  "id": 15
}
📦 Get Order
Authorization: Bearer token required
Endpoint: GET http://{host}:8001/api/order/15
Response:
{
  "id": 10,
  "sku": "11222511",
  "name": "cellphone",
  "price": "2323.21",
  "delivery_date": "01-01-2024",
  "status": "DELAYED"
}
