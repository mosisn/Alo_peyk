from .models import Origin, Destination, Order
from rest_framework.response import Response
from rest_framework import status
from user.authentication import JWTAuthentication
from rest_framework import generics
import random
from .serializers import OrderSerializer


def generate_tracking_code():
    random_code = random.randint(10000,99999)
    try:
        Order.objects.get(Tracking_code=random_code)
        generate_tracking_code()
    except:
        return random_code
    

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
