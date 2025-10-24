from django.db import models

# Create your models here.
# Model 1: Learning Journey
class LearningJourney(models.Model):
    year = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.title}"


# Model 2: Feedback
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.name}"


# Model 3: Skill or Achievement
class Skill(models.Model):
    skill_name = models.CharField(max_length=100)
    level = models.CharField(
        max_length=50,
        choices=[
            ('Beginner', 'Beginner'),
            ('Intermediate', 'Intermediate'),
            ('Advanced', 'Advanced'),
        ]
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.skill_name