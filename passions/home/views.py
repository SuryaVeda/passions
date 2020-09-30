from django.shortcuts import render, redirect
from music.models import Youtube
from django.utils import timezone
from .models import News
from .forms import LessonForm
from gym.models import Lessons
from travel.models import Travel
from new.models import Book, Page
import datetime
from datetime import date, timedelta
from urllib.parse import urljoin
import requests, facebook
from itertools import chain
from home.decorators import admin_required

graph = facebook.GraphAPI(access_token="EAAHlA6rZAYkgBAAPwZBmWd8xzhA1AjTOhtRMZCAP95K5p0f7IanZA0PzjZCR2ec2ArhRUwq2GzMQlDzlj9FmsRRKFtl4SItLmXBzqGlRCt4XRKxauOqU4HhLtFAsZCdKG6xZBnkh4jDg3D2tSkVcLdt0EiHUMfsvetAX2C6hi9DKQZDZD", version="3.1")
page_id = '102395031101655'

# Create your views here.
def home(request):
	template_name = 'home/home.html'
	today = datetime.date.today()
	past_week = today - timedelta(days=7)
	week = today + timedelta(days=7)
	travel = Travel.objects.filter(date__range = [past_week, week])
	videos = Youtube.objects.filter(date__range = [past_week, week])
	lessons = Lessons.objects.filter(date__range = [past_week, week])
	news = News.objects.filter(date__range = [past_week, week])
	context = {'travel':travel,'videos':videos, 'lessons':lessons, 'news':news}
	return render(request, template_name, context)

@admin_required
def add_lesson(request):
	template_name = 'home/newsForm.html'
	form = LessonForm()
	if request.method == "POST":
		form = LessonForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['heading']
			description = form.cleaned_data['description']
			form = form.save(commit = False)
			if request.user.admin:
				form.user=request.user
				form.date = timezone.now()
				form.save()
				post = News.objects.get(heading=name, description=description)
				post_url = 'https://mypassions.site/stories'
				image_url = '/home/surya/passions/passions' + post.image.url
				graph.put_photo(image=open(image_url, 'rb'), message = 'News @' + post.heading + '.      Check out the url for complete article.' + post_url )
				return redirect('stories:main')
			else:
				return redirect('home:home')
		else:
			form = LessonForm()
	return render(request, template_name, {'form':form})
@admin_required
def edit_lesson(request, pk):
	template_name = 'home/newsForm.html'
	instance = News.objects.get(pk = pk)
	form = LessonForm(instance=instance)
	if request.method == "POST":
		form = LessonForm(request.POST, request.FILES, instance = instance)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user.admin:
				form.save()
				return redirect('stories:main')
			else:
				return redirect('home:home')
		else:
			form = LessonForm(instance=instance)
	return render(request, template_name, {'form':form})


def search(request):
	if request.method == 'GET':
		query = request.GET.get('search')
		if not query:

			message = 'No query entered'
			template_name = 'home/home.html'
			today = datetime.date.today()
			past_week = today - timedelta(days=7)
			week = today + timedelta(days=7)
			travel = Travel.objects.filter(date__range = [past_week, week])
			videos = Youtube.objects.filter(date__range = [past_week, week])
			lessons = Lessons.objects.filter(date__range = [past_week, week])
			news = News.objects.filter(date__range = [past_week, week])
			context = {'travel':travel,'videos':videos, 'lessons':lessons,'news':news, 'message':message}
			return render(request, template_name, context)
		else:
			music = Youtube.objects.search(query)
			gym = Lessons.objects.search(query)
			travel = Travel.objects.search(query)
			stories = Book.objects.search(query)
			news = News.objects.search(query)
			results = list(chain(music, gym, travel, stories, news))
			if not results:
				message = 'No Results for Query'
				template_name = 'home/home.html'
				today = datetime.date.today()
				past_week = today - timedelta(days=7)
				week = today + timedelta(days=7)
				travel = Travel.objects.filter(date__range = [past_week, week])
				videos = Youtube.objects.filter(date__range = [past_week, week])
				lessons = Lessons.objects.filter(date__range = [past_week, week])
				news = News.objects.filter(date__range = [past_week, week])
				context = {'travel':travel,'videos':videos, 'lessons':lessons,'news':news, 'message':message}
				return render(request, template_name, context)
			return render(request, 'home/home.html', {'results':results, 'music':music, 'gym':gym, 'stories':stories,'news':news, 'travel':travel})

	else:
		return redirect('home:home')