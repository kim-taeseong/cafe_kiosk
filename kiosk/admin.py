from django.contrib import admin
from .models import Category, Item

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'updated_date')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'created_date', 'updated_date')
