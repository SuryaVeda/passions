from django.db import models
import datetime
import json
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils import timezone
# Create your models here.
class BookSearchManager(models.Manager):
	def search(self, query):
		return Book.objects.filter(name__icontains=query)
class PagesSearchManager(models.Manager):
	def search(self, query):
		return Page.objects.filter(heading__icontains=query)

class Book(models.Model):
	name = models.CharField(max_length = 30)
	author = models.CharField(max_length = 30)
	date_created = models.DateField(default = timezone.now())
	date_completed = models.DateField(blank=True, null = True)
	image = models.ImageField(blank=False, null = True, upload_to = 'images/%Y/%m/')
	summary = models.TextField(blank = True, null = True)
	draft = models.BooleanField(default=False)
	objects = BookSearchManager()
	def set_authors(self, x):
		self.author = json.dumps(x)
	def get_authors(self):
		return json.loads(self.author)
	def get_length(self):
		return len(self.get_authors())
	def get_pages(self):
		return len(self.page_set.all())
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
		if self.image:
			self.image = self.compressImage(self.image)
			super(Book, self).save(*args, **kwargs)
		super(Book, self).save(*args, **kwargs)

class Page(models.Model):
	book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank = True)
	heading = models.CharField(max_length = 30, blank=True, null = True)
	para = models.CharField(max_length=6000, blank = True, null = True)
	image = models.ImageField(blank=True, null = True, upload_to = 'images/%Y/%m/$D/')
	draft = models.BooleanField(default=False)
	objects = PagesSearchManager()
	pageno = models.IntegerField()
	def set_para(self, x):
		self.para = json.dumps(x)
	def get_para(self):

		return json.loads(self.para)
	def get_length(self):
		return len(self.para)
	def __str__(self):
		return str(self.pk)
	def compressImage(self,uploadedImage):
		im = Image.open(uploadedImage)
		output = BytesIO()
		im = im.resize( (900,600) ) 
		im.save(output , format='JPEG', quality=40)
		output.seek(0)
		newImage = InMemoryUploadedFile(output,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		return newImage
	def PageNumber(self):
		a = Book.objects.get(name = self.book.name)
		query_set = a.page_set.order_by('pk')
		count = query_set.count()
		if count>=1:
			pageno = count + 1
			return pageno
		else:
			pageno = 1
			return pageno

	def save(self, *args, **kwargs):
		if self.image:
			self.image = self.compressImage(self.image)
			self.pageno=self.PageNumber()
			super(Page, self).save(*args, **kwargs)
		self.pageno=self.PageNumber()
		super(Page, self).save(*args, **kwargs)

