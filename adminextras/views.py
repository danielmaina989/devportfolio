from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.views.generic.edit import FormView
from django.utils import timezone
from portfolio.models import ContactMessage
from .forms import ReplyForm
from django.urls import reverse_lazy

class ReplyView(FormView):
    template_name = 'adminextras/reply_contact.html'
    form_class = ReplyForm
    success_url = reverse_lazy('admin:index')

    def dispatch(self, request, *args, **kwargs):
        self.message = get_object_or_404(ContactMessage, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        reply_message = form.cleaned_data['reply']
        recipient = self.message.email
        attachment = form.cleaned_data.get('attachment')

        # Create an email message
        email = EmailMessage(
            subject,
            reply_message,
            'your@email.com',
            [recipient],
        )

        # Attach the file if it's provided
        if attachment:
            email.attach(attachment.name, attachment.read(), attachment.content_type)

        # Send the email
        email.send(fail_silently=False)

        # Update the ContactMessage instance
        self.message.replied = True
        self.message.reply_message = reply_message
        self.message.replied_at = timezone.now()

        if attachment:
            # Save the attachment to the document field
            self.message.document = attachment

        self.message.save()

        messages.success(self.request, "Reply sent successfully.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = self.message
        return context
