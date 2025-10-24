from django.shortcuts import render
from .models import LearningJourney, Feedback, Skill

# Create your views here.
# Home Page View
def index(request):
    journeys = LearningJourney.objects.all().order_by('year')
    return render(request, 'index.html', {'journeys': journeys})

# About Me Page View
def aboutMe(request):
    skills = Skill.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'aboutMe.html', {'skills': skills, 'feedbacks': feedbacks})





