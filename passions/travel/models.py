from django.db import models
from django.conf import settings
import datetime
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils import timezone

# Create your models here.
class SearchManager(models.Manager):
	def search(self, query):
		return Travel.objects.filter(name__icontains=query)

class Travel(models.Model):
	date = models.DateField(default = timezone.now())
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null = True)
	name = models.CharField(max_length = 50)
	why = models.TextField(blank = True, null = True)
	fun = models.TextField(null = True, blank = True)
	how = models.TextField(blank = True, null = True)
	img1 = models.ImageField(blank=False, null = True, upload_to = 'Travel/%Y/%m/')
	img2 = models.ImageField(blank=True, null = True, upload_to = 'Travel/%Y/%m/')
	img3 = models.ImageField(blank=True, null = True, upload_to = 'Travel/%Y/%m/')
	img4 = models.ImageField(blank=True, null = True, upload_to = 'Travel/%Y/%m/')
	links = models.URLField(max_length=500, blank = True, null = True)
	objects = SearchManager()

	def __str__(self):
		return self.name
	def compressImage(self,uploadedImage):
		im = Image.open(uploadedImage)
		output = BytesIO()
		im = im.resize( (900,600) ) 
		im.save(output , format='JPEG', quality=40)
		output.seek(0)
		newImage = InMemoryUploadedFile(output,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		return newImage

	def save(self, *args, **kwargs):
		if self.img1:
			self.img1 = self.compressImage(self.img1)
			super(Travel, self).save(*args, **kwargs)
		if self.img2:
			self.img2 = self.compressImage(self.img2)
			super(Travel, self).save(*args, **kwargs)
		if self.img3:
			self.img3 = self.compressImage(self.img3)
			super(Travel, self).save(*args, **kwargs)
		if self.img4:
			self.img4 = self.compressImage(self.img4)
			super(Travel, self).save(*args, **kwargs)
		super(Travel, self).save(*args, **kwargs)
