from django.db import models
from urllib.parse import urlparse, parse_qs
import datetime
from accounts.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils import timezone

# Create your models here.
class SearchManager(models.Manager):
	def search(self, query):
		return Lessons.objects.filter(name__icontains=query)


class Lessons(models.Model):
	user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank = True)
	date = models.DateField(default = timezone.now())
	name = models.CharField(max_length=20, null = False, blank = False)
	description = models.TextField(max_length = 700, null = True, blank = True)
	images = models.ImageField(blank=True, null = True, upload_to = 'gym/%Y/%m/')
	description2 = models.TextField(max_length = 700, null = True, blank = True)
	description3 = models.TextField(max_length = 700, null = True, blank = True)
	description4 = models.TextField(max_length = 700, null = True, blank = True)
	img2 = models.ImageField(blank=True, null = True, upload_to = 'gym/%Y/%m/')
	img3 = models.ImageField(blank=True, null = True, upload_to = 'gym/%Y/%m/')
	img4 = models.ImageField(blank=True, null = True, upload_to = 'gym/%Y/%m/')
	url = models.URLField(max_length = 800, blank=True, null = True)
	objects = SearchManager()
	def __str__(self):
		return self.name

	def get_code(self):
		a = urlparse(self.url)
		dic = parse_qs(a.query)
		b = dic.get('v')
		path = a.path.split('/')
		if a.query=="":
			return path[1]
		else:
			return b[0]
	def compressImage(self,uploadedImage):
		im = Image.open(uploadedImage)
		output = BytesIO()
		im = im.resize( (900,600) ) 
		im.save(output , format='JPEG', quality=40)
		output.seek(0)
		newImage = InMemoryUploadedFile(output,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		return newImage

	def save(self, *args, **kwargs):
		if self.images:
			self.images = self.compressImage(self.images)
			super(Lessons, self).save(*args, **kwargs)
		if self.img2:
			self.img2 = self.compressImage(self.img2)
			super(Lessons, self).save(*args, **kwargs)
		if self.img3:
			self.img3 = self.compressImage(self.img3)
			super(Lessons, self).save(*args, **kwargs)
		if self.img4:
			self.img4 = self.compressImage(self.img4)
			super(Lessons, self).save(*args, **kwargs)

		super(Lessons, self).save(*args, **kwargs)
