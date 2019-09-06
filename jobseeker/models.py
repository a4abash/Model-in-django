from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class jobseeker(models.Model):
    address = models.CharField(max_length=100)
    experience_year = models.IntegerField(null=True,blank=True)
    professional_title = models.CharField(max_length=100)
    portfolio = models.URLField(null=True,blank=True)
    about = models.TextField()
    cv = models.FileField(upload_to='cv/', null=True , blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class skill(models.Model):
    title = models.CharField(max_length=100)
    jobseeker = models.ForeignKey(jobseeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobseeker.user.username

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    jobseeker = models.ForeignKey(jobseeker,on_delete=models.CASCADE)

    def __str__(self):
        return self.jobseeker.user.username

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(null=True,blank=True)
    jobseeker = models.ForeignKey(jobseeker,on_delete=models.CASCADE)

    def __str__(self):
        return self.jobseeker.user.username