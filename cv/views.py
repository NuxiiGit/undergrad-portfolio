from django.shortcuts import render
from .models import Contact, Skill, Experience, Education

def display_cv(request):
	contacts = Contact.objects.all()
	skills = Skill.objects.all()
	experiences = Experience.objects.all().order_by('end_date')
	educations = Experience.objects.all().order_by('end_date')
	return render(request, 'cv/display_cv.html', {
		'contacts' : contacts,
		'skills' : skills,
		'experiences' : experiences,
		'educations' : educations
	})