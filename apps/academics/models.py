from django.db import models
from apps.authentication.models import StudentProfile
from django.db.models.signals import post_save
from django.dispatch import receiver

class Subject(models.Model):
    NAME_CHOICES = [
        ('MATH', 'Mathematics'), ('MTHL', 'Mathematical Literacy'),
        ('PHYS', 'Physical Sciences'), ('LFSC', 'Life Sciences'),
        ('ENGL', 'English Home Language'), ('FAL', 'First Additional Language'),
        ('ACC', 'Accounting'), ('IT', 'Information Technology'), ('CAT', 'Computer Applications Technology')
    ]
    name = models.CharField(max_length=4, choices=NAME_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class TermMark(models.Model):
    TERM_CHOICES = [(1, 'Term 1'), (2, 'Term 2'), (3, 'Term 3'), (4, 'Term 4')]

    profile = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    percentage = models.IntegerField()
    term = models.IntegerField(choices=TERM_CHOICES)
    year = models.IntegerField(default=2026)

    class Meta:
        unique_together = ('profile', 'subject', 'term', 'year')

# --- Gamification Signal Engine ---
@receiver(post_save, sender=TermMark)
def award_xp_for_marks(sender, instance, created, **kwargs):
    """Dynamically updates student XP and Levels based on academic entries."""
    profile = instance.profile
    if created:
        # Base XP for entering marks
        profile.xp_points += 50 
        
        # Performance bonus XP
        if instance.percentage >= 75:
            profile.xp_points += 100  # Distinction bonus
        elif instance.percentage >= 50:
            profile.xp_points += 30
            
    # Simple leveling logic (Every 200 XP = 1 Level Up)
    profile.level = (profile.xp_points // 200) + 1
    profile.save()