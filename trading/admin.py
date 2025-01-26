from django.contrib import admin

from trading.models import ContactInfo, Product, Vendor
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "User" в административной панели"""

    list_display = (
        'pk',
        'email',
        'first_name',
        'last_name',
        'phone',
        'is_active',
        'date_joined',
        'last_login',
    )

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "ContactInfo" в административной панели"""
    list_display = (
        'pk',
        'email',
        'country',
        'city',
        'street',
        'house_number',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Product" в административной панели"""
    list_display = (
        'pk',
        'title',
        'model',
        'launched_at',
    )


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Vendor" в административной панели"""
    list_display = (
        'pk',
        'title',
        'level',
        'debt_to_supplier',
        'contact',
        'created_at',
    )
