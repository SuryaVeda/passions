from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Stories(models.Model):
	date = models.DateField(default = timezone.now())
	name = models.CharField(max_length=50, blank = False, null = False)
	summary = models.TextField( blank = False, null = False)
	image = models.ImageField(blank=True, null = True, upload_to = 'stories/%Y/%m/')
	pdf = models.FileField(blank=True, null = True, upload_to = 'stories/pdf/%Y/%m/$D/')
	def __str__(self):
		return self.name
