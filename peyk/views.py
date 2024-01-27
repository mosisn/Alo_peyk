from .models import Origin, Destination, Order
from rest_framework.response import Response
from rest_framework import status
from user.authentication import JWTAuthentication
from rest_framework import generics
import random
from .serializers import OrderSerializer, OriginSerializer, DestinationSerializer
import requests

def get_address():
    address = 'تهران، خ. هفده شهریور، بعد از چهارراه شکوفه'
    url = f'https://api.neshan.org/v4/geocoding?address={address}'
    api = requests.get(headers={'Api-key' : 'web.c2831504fd404ae6b5346f2b59272a6e'}, url=url).json()
    return api

    
    

def generate_tracking_code():
    random_code = random.randint(10000,99999)
    try:
        Order.objects.get(Tracking_code=random_code)
        generate_tracking_code()
    except:
        return random_code
    
class CreateOrigin(generics.CreateAPIView):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer
    authentication_classes = [JWTAuthentication,]

    def list(self, request, *args, **kwargs):
        self.queryset = Origin.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)

class CreateDestination(generics.CreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    authentication_classes = [JWTAuthentication,]

    def list(self, request, *args, **kwargs):
        self.queryset = Destination.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)

class OriginView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

class DestinationView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = self.perform_create(serializer, request)
        headers = self.get_success_headers(serializer.data)
        return Response("Order Reserved with {} tracking code!".format(code), status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, request):
        code = generate_tracking_code()
        serializer.save(
            tracking_code = code,
            user = request.user
        )
        return code

class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication,]

    def list(self, request, *args, **kwargs):
        self.queryset = Order.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)