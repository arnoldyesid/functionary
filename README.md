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

# Register
{{host}} by default: localhost

curl --location --request POST '{{host}}:8001/api/user/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "test", 
    "email":"test@gmail.com",
    "password":"12345678"
}'
Response:
{
    "name": "Arnold",
    "email": "test@gmail.com"
}
--------------------------------------------------------------------

# Login
curl --location --request POST '{{host}}:8001/api/user/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email":"user@gmail.com",
    "password":"12345678"
}'
Response:
{
    "access": "eyJ0e.."
}
--------------------------------------------------------------------

# Create Order 
curl --location --request POST '{{host}}:8001/api/order/new' \
--header 'Authorization: Bearer eyJ.... \
--header 'Content-Type: application/json' \
--data-raw '{
    "sku": "1922511",
    "name": "cellphone",
    "price": 2323.21,
    "delivery_date": "01-01-2024"
}'
# Response 
{
    "id": 15
}
--------------------------------------------------------------------

# Get order 
curl --location --request GET '{{host}}:8001/api/order/{order_id}' \
--header 'Authorization: Bearer eyJ0e...

# Response 
{
    "id": 10,
    "sku": "11222511",
    "name": "cellphone",
    "price": "2323.21",
    "delivery_date": "01-01-2024",
    "status": "DELAYED"
}