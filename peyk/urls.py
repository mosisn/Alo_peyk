from django.urls import path
from .views import OrderCreate

urlpatterns = [
    path('new', OrderCreate.as_view(),name='OrderCreate')
]