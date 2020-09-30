from django.db import models
from urllib.parse import urlparse, parse_qs
import datetime
from accounts.models import User
# Create your models here.
from django.utils import timezone

class SearchManager(models.Manager):
	def search(self, query):
		return Youtube.objects.filter(name__icontains=query)


class Youtube(models.Model):
	user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank = True)
	date = models.DateField(default = timezone.now())
	name = models.CharField(max_length=50, blank= False, null = False, default = "Hello!")
	description = models.TextField(blank=True, null = True)
	url = models.URLField(max_length = 800, blank=True, null = True)
	image = models.ImageField(blank=False, null = True, upload_to = 'music/%Y/%m/$D/')
	pdf = models.FileField(blank=True, null = True, upload_to = 'music/pdf/%Y/%m/$D/')
	objects = SearchManager()

	def __str__(self):
		return self.name
	@property	
	def get_code(self):
		if self.url:
		    a = urlparse(self.url)
		    dic = parse_qs(a.query)
		    b = dic.get('v')
		    path = a.path.split('/')
		    if a.query=="":
			    return path[1]
		    else:
			    return b[0]
		
		
    


