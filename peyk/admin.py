from django.contrib.admin import ModelAdmin, register
from .models import Province, City, Origin, Destination, Order


@register(Province)
class ProvinceAdmin(ModelAdmin):
    pass


@register(City)
class CityAdmin(ModelAdmin):
    pass


@register(Origin)
class OriginAdmin(ModelAdmin):
    pass


@register(Destination)
class DestinationAdmin(ModelAdmin):
    pass


@register(Order)
class OrderAdmin(ModelAdmin):
    pass

