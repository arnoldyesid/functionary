# functionary
#Requirments 
- Docker version 24.0.2
- make

# Run service
1- cd E-commer-project-main
2 -[Run buld and services] make build
After point 2 you can use the enpoints 

3 -[Run test] make test
4 - [Run check due orders] make check_past_due_orders

# Endpoints
{host} by default: localhost
--------------------------------------------------------------------
# Register
POST: http://{host}:8001/api/user/register

body:
{
    "name": "Arnold", 
    "email":"ar12no21ldw.blandon3@gmail.com",
    "password":"12345678"
}

Response:
{
    "name": "TEST",
    "email": "test@gmail.com"
}
--------------------------------------------------------------------
# Login
POST: http://{host}:8001/api/user/login
Body:
{
    "email":"user@gmail.com",
    "password":"12345678"
}
Response:
{
    "access": "eyJ0e.."
}
--------------------------------------------------------------------
# Create Order 
Required:  Authorization: Bearer 
POST: http://{host}:8001/api/order/new
body
{
    "sku": "2922511",
    "name": "cellphone",
    "price": 2323.21,
    "delivery_date": "01-01-2024"
}
# Response 
{
    "id": 15
}
--------------------------------------------------------------------

# Get order 
Required:  Authorization: Bearer 
GET: http://{host}:8001/api/order/15
# Response 
{
    "id": 10,
    "sku": "11222511",
    "name": "cellphone",
    "price": "2323.21",
    "delivery_date": "01-01-2024",
    "status": "DELAYED"
}