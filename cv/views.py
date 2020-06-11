from django.shortcuts import render
from .models import Contact, Skill, Experience, Education

def display_cv(request):
	return render(request, 'blog/base.html', { })