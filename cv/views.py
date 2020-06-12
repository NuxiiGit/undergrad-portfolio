from django.shortcuts import render
from .models import Contact, Skill, Experience, Education

def display_cv(request):
	skills = Skill.objects.all()
	return render(request, 'cv/display_cv.html', { 'skills' : skills })