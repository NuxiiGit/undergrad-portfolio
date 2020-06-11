from django.urls import path
from . import views

urlpatterns = [
	path('', views.display_cv, name='display_cv')
]