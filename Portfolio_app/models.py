from django.db import models

# Create your models here.
class Projects(models.Model):
    projectName = models.CharField(max_length=100)
    fileProject = models.FileField(upload_to='')