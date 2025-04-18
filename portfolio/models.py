from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    document = models.FileField(upload_to='contact_docs/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    

# models.py

# models.py

class TeamMember(models.Model):
    CATEGORY_CHOICES = [
        ('developer', 'Developer'),
        ('designer', 'UI/UX Designer'),
        ('project_manager', 'Project Manager'),
        ('qa', 'QA Engineer'),
        ('devops', 'DevOps Engineer'),
        ('product', 'Product Manager'),
        ('marketing', 'Marketing Specialist'),
        ('support', 'Technical Support'),
        ('sales', 'Sales Representative'),
    ]


    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,  default='developer')
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team_photos/')
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.role}"


