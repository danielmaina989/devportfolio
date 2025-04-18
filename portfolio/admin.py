from django.contrib import admin
from .models import ContactMessage, TeamMember

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'message')



admin.site.register(TeamMember)
