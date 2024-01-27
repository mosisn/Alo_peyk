from django.urls import path
from .views import OrderCreate, OrderView, CreateOrigin,OriginView,DestinationView,CreateDestination

urlpatterns = [
    path('new', OrderCreate.as_view(),name='OrderCreate'),
]