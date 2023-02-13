from django.contrib import admin
from src.marketplace.models import (
    Item,
    OrderItem,
    Order
)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """ Item administration
    """
    list_display = ['name', 'description', 'price']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price']
    ordering = ['name', 'price']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """ OrderItem administration
    """
    list_display = ['buyer', 'created', 'updated', 'quantity']
    list_filter = ['buyer', 'created']
    search_fields = ['buyer', 'created']
    ordering = ['created']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Orders administration
    """
    list_display = ['buyer', 'status', 'created', 'updated']
    list_filter = ['buyer', 'status', 'created']
    search_fields = ['buyer', 'status', 'created']
    ordering = ['status', 'created']