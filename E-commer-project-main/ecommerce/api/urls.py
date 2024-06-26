from django.urls import path, include
from .views import (
    RegisterView,
    LoginView,
    OrderCreateView,
    OrderViewSet
)
urlpatterns = [
    path('user/register', RegisterView.as_view({'post': 'register'}), name='user-register'),
    path('user/login', LoginView.as_view({'post': 'login'}), name='user-login'),
    path('order/new', OrderCreateView.as_view({'post': 'order'}), name='order-new'),
    path('order/<int:id>', OrderViewSet.as_view({'get': 'order'}), name='order-detail'),
]
