from django.contrib import admin
from .models import Header

# Register your models here.

class HeaderAdmin(admin.ModelAdmin):
    list = ('header1','header2','header3','header4','header5','header6')

    admin.site.register(Header)
