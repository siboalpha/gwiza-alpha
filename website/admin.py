from django.contrib import admin
from .models import ContactMessage
# Register your models here.

@admin.register(ContactMessage)
class ContactMessage(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number", "email")