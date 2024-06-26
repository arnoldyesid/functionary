from celery import shared_task
from datetime import date

from commun.enums import OrderStatus
from .models import Order


@shared_task
def check_past_due_orders():
    DELAYED = OrderStatus.DELAYED.value
    current_date = date.today()
    past_due_orders = Order.objects.filter(
        delivery_date__lt=current_date,
        status=OrderStatus.CREATED.value
    )
    for order in past_due_orders:
        order.status = DELAYED
        order.save()
    return f"Updated {past_due_orders.count()} orders to {DELAYED} status."
