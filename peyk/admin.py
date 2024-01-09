from django.contrib.admin import ModelAdmin, register
from .models import  Origin, Destination, Order


@register(Origin)
class OriginAdmin(ModelAdmin):
    pass


@register(Destination)
class DestinationAdmin(ModelAdmin):
    pass


@register(Order)
class OrderAdmin(ModelAdmin):
    pass

