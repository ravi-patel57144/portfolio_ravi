import os

from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=500)


class Docs(models.Model):
    resume = models.FileField(upload_to='resume/', validators=[FileExtensionValidator(['pdf'])],
                              help_text='File Must Be in PDF format')
    github = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.CharField(max_length=200, blank=True, null=True)
