from django.contrib import admin
from src.marketplace.models import Item, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """ Item administration
    """
    list_display = ['name', 'description', 'price']
    list_filter = ['name', 'price']
    search_fields = ['name', 'price']
    ordering = ['name', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Order administration
    """
    list_display = ['buyer', 'status', 'created', 'updated', 'quantity']
    list_filter = ['buyer', 'status', 'created']
    search_fields = ['buyer', 'status', 'created']
    ordering = ['status', 'created']
