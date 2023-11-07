from django.contrib import admin
from book.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ['first_name', "last_name", 'email' , 'city','from_time','appointed_date',]
    search_fields = ('first_name',)
    # date_hierarchy = 'from_time'
    ordering = ('-pk',)