from django.contrib import admin
from .models import jobseeker,skill,Experience,Project
# Register your models here.
admin.site.register(jobseeker)
admin.site.register(skill)
admin.site.register(Experience)
admin.site.register(Project)