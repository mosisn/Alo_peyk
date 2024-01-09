from rest_framework.serializers import ModelSerializer, CharField
from .models import Order,Origin,Destination

class OriginSerializer(ModelSerializer):
    class Meta:
        model = Origin
        fields = '__all__'

class DestinationSerializer(ModelSerializer):
    origin = OriginSerializer()
    class Meta:
        model = Destination
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    tracking_code = CharField(required=False)
    user = CharField(required=False)
    class Meta:
        model = Order
        fields = '__all__'