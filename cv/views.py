from django.shortcuts import render
from .models import Name, Contact, Skill, Experience, Education

def display_cv(request):
	names = Name.objects.all()
	contacts = Contact.objects.all()
	skills = Skill.objects.all()
	experiences = Experience.objects.all().order_by('-start_date')
	educations = Education.objects.all().order_by('-start_date')
	return render(request, 'cv/display_cv.html', {
		'names' : names,
		'contacts' : contacts,
		'skills' : skills,
		'experiences' : experiences,
		'educations' : educations
	})