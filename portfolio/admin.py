from django.contrib import admin
from .models import ContactMessage, TeamMember
from django.urls import path, reverse_lazy
from django.utils.html import format_html
from adminextras.views import ReplyView

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at', 'replied', 'reply_link', 'document_link']

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'reply/<int:pk>/',
                self.admin_site.admin_view(ReplyView.as_view()),  # ✅ FIXED
                name='contactmessage-reply'
            ),
        ]
        return custom_urls + urls

    def reply_link(self, obj):
        return format_html(
            '<a class="button" href="{}">Reply</a>',
            reverse_lazy('admin:contactmessage-reply', args=[obj.pk])
        )

    def document_link(self, obj):
        if obj.document:
            # Generate a link to the document if it exists
            return format_html(
                '<a href="{}" target="_blank">View Document</a>',
                obj.document.url
            )
        return 'No document'

    reply_link.short_description = 'Reply Action'
    document_link.short_description = 'Document'
    reply_link.allow_tags = True

admin.site.register(TeamMember)
