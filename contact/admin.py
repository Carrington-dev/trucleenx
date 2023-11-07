from django.contrib import admin

from contact.models import Contact, Subscribe
from myauth.admin import export_to_csv


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'phone', 'message', 'date_recieved', 'date_last_viewed')
    list_filter = ('name', 'email',)
    readonly_fields = ('message',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page: int = 30


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_subscribed', 'date_recieved', 'date_last_viewed')
    list_filter = ('is_subscribed',)
    search_fields = ('email', )
    date_hierarchy = 'date_recieved'
    ordering = ('-pk',)
    list_per_page: int = 30
    actions = [export_to_csv]