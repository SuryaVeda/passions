from django.db import models
from accounts.models import User
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.utils import timezone
from urllib.parse import urlparse, parse_qs
import datetime

# Create your models here.
class SearchManager(models.Manager):
	def search(self, query):
		return News.objects.filter(heading__icontains=query)

class Category(models.Model):
	name = models.CharField(max_length= 50, default= "Other")
	def __str__(self):
		return self.name

class News(models.Model):
	category = models.ForeignKey(Category, on_delete= models.SET_NULL, null = True, blank = True)
	user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank = True)
	date = models.DateField(default = timezone.now())
	heading = models.CharField(max_length = 150)
	description = models.TextField()
	url = models.URLField(max_length = 800, blank=True, null = True)
	url2 = models.URLField(max_length = 800, blank=True, null = True)
	image = models.ImageField(blank=False, null = True, upload_to = 'home/news/%Y/%m/')
	objects = SearchManager()

	def __str__(self):
		return self.heading
	def compressImage(self,uploadedImage):
		im = Image.open(uploadedImage)
		output = BytesIO()
		im = im.resize( (900,600) ) 
		im.save(output , format='JPEG', quality=60)
		output.seek(0)
		newImage = InMemoryUploadedFile(output,'ImageField', "%s.jpg" % uploadedImage.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		return newImage

	def save(self, *args, **kwargs):
		if self.image:
			self.image = self.compressImage(self.image)
			super(News, self).save(*args, **kwargs)
	
		super(News, self).save(*args, **kwargs)

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


class Comment(models.Model):
	pk_comment = models.IntegerField(default=1)
	travel = models.BooleanField(default=False)
	gym = models.BooleanField(default=False)
	music = models.BooleanField(default=False)
	news = models.BooleanField(default=False)
	stories = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank = True)
	date = models.DateField(default = timezone.now())
	description = models.TextField()
	def __str__(self):
		return self.description
	@property
	def get_replies(self):
		return len(self.reply_set.all())

	@property
	def since(self):
		since_time = (timezone.now().date() - self.date).days
		if since_time >= 1:
			return str(since_time) + '  days ago....' 
		else:
			return 'Published Today'
	
	

	

class Reply(models.Model):
	user = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank = True)
	date = models.DateField(default = timezone.now())	
	comment = models.ForeignKey(Comment, on_delete= models.SET_NULL, null = True, blank = True)
	description = models.TextField()
	def __str__(self):
		return self.description
	@property
	def since(self):
		since_time = (timezone.now().date() - self.date).days
		if since_time >= 1:
			return str(since_time) + '  days ago...' 
		else:
			return 'Published Today'



