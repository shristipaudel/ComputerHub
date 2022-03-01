from django.contrib import admin

# Register your models here.
from .models import ComputerBrands
from .models import ComputerSpecification
from .models import Order


class AdminComputerBrands(admin.ModelAdmin):
    list_display = ['brandname', 'logo']


admin.site.register(ComputerBrands, AdminComputerBrands)


class AdminComputerSpecification(admin.ModelAdmin):
    list_display = ['generation', 'price_min', 'price_max', 'ram', 'brandname','computercode']


admin.site.register(ComputerSpecification, AdminComputerSpecification)

class AdminOrder(admin.ModelAdmin):
    list_display = ['computercode', 'brandname', 'quantity', 'unitrate', 'totalprice']


admin.site.register(Order, AdminOrder)