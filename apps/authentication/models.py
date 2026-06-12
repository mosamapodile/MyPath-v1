from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Custom user model in case we need to add phone authentication later."""
    pass

class StudentProfile(models.Model):
    PROVINCE_CHOICES = [
        ('EC', 'Eastern Cape'), ('FS', 'Free State'), ('GP', 'Gauteng'),
        ('KZN', 'KwaZulu-Natal'), ('LP', 'Limpopo'), ('MP', 'Mpumalanga'),
        ('NC', 'Northern Cape'), ('NW', 'North West'), ('WC', 'Western Cape'),
    ]
    
    GRADE_CHOICES = [(10, 'Grade 10'), (11, 'Grade 11'), (12, 'Grade 12')]

    # To this (related_name):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    grade = models.IntegerField(choices=GRADE_CHOICES)
    province = models.CharField(max_length=3, choices=PROVINCE_CHOICES)
    xp_points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Grade {self.grade}"