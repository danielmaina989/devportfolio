from django import forms


class ReplyForm(forms.Form):
    
    subject = forms.CharField(
        max_length=255,
        label="Email Subject",
        widget=forms.TextInput(attrs={'placeholder': 'Enter subject here'}),
    )
    reply = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'placeholder': 'Write your reply here...'}),
    )
    attachment = forms.FileField(
        required=False,
        label="Attach PDF or DOCX file (optional)",
    )

    def clean_attachment(self):
        file = self.cleaned_data.get('attachment')

        if file:
            if not file.name.lower().endswith(('.pdf', '.docx')):
                raise forms.ValidationError("Only PDF or DOCX files are allowed.")
            if file.size > 5 * 1024 * 1024:  # 5MB limit
                raise forms.ValidationError("File size exceeds the 5MB limit.")
        return file
