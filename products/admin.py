from django.contrib import admin
from .models import Products, Category, Color, Size


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "stock"]
    list_filter = ["category", "color", "size"]
    search_fields = ["title"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ["name"]
