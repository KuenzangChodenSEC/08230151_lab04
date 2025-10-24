from django.contrib import admin
from .models import LearningJourney, Feedback, Skill

# Register your models here.
admin.site.register(LearningJourney)
admin.site.register(Feedback)
admin.site.register(Skill)