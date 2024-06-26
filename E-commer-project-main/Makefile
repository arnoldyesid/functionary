SHELL := /bin/bash

run_task:
	docker exec -it ecommerce_container python manage.py shell -c "from api.tasks import check_past_due_orders; check_past_due_orders.delay()"
build:
	docker-compose up -d --build

migrate_and_run:
	docker exec -it ecommerce_container bash -c "python manage.py makemigrations &&  python manage.py migrate"

run_app:
	docker exec -it ecommerce_container bash -c "python manage.py runserver 0.0.0.0:8000"

test:
	docker exec -it ecommerce_container bash -c "python manage.py test"
