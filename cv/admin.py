from django.contrib import admin
from .models import Name, Contact, Skill, Experience, Education

admin.site.register(Name)
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)