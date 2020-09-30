from django.shortcuts import render, redirect
from .models import Lessons
from .forms import LessonForm, EditLessonForm
import facebook
from django.contrib.auth.decorators import login_required
from home.decorators import admin_required
from home.models import Comment, Reply
from home.forms import CommentForm, ReplyForm
from django.utils import timezone
# Create your views here.
graph = facebook.GraphAPI(access_token="EAAHlA6rZAYkgBAAPwZBmWd8xzhA1AjTOhtRMZCAP95K5p0f7IanZA0PzjZCR2ec2ArhRUwq2GzMQlDzlj9FmsRRKFtl4SItLmXBzqGlRCt4XRKxauOqU4HhLtFAsZCdKG6xZBnkh4jDg3D2tSkVcLdt0EiHUMfsvetAX2C6hi9DKQZDZD", version="3.1")
page_id = '102395031101655'


def cook(request):
	template_name = 'home/gym.html'
	lessons = Lessons.objects.order_by('pk')
	context = {'lessons':lessons}
	return render(request, template_name, context)
def details(request, pk):
	template_name = 'home/gym_detail.html'
	lessons = Lessons.objects.order_by('pk')
	post = Lessons.objects.get(pk=pk)
	form = CommentForm()
	replyForm = ReplyForm()
	comments = Comment.objects.filter(gym=True, pk_comment=pk)
	replies = Reply.objects.order_by('pk')
	comment_length = len(comments)
	context = {'post':post, 'lessons':lessons, 'form':form, 'replyForm':replyForm, 'comments':comments, 'replies':replies,  'comment_length':comment_length}
	return render(request, template_name, context)
@admin_required
def add_lesson(request):
	template_name = 'home/lessonForm.html'
	form = LessonForm()
	if request.method == "POST":
		form = LessonForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			form = form.save(commit = False)
			if request.user:
				form.user=request.user
				form.date = timezone.now()
				form.save()
				post = Lessons.objects.get(name=name, description=description)
				post_url = 'https://mypassions.site/gym/'
				image_url = '/home/surya/passions/passions' + post.images.url
				graph.put_photo(image=open(image_url, 'rb'), message = 'SimpleTips @' + post.name + '.      Check out the url for complete article.' + post_url )
				return redirect('gym:main')
			else:
				return redirect('home:home')
		else:
			form = LessonForm()
	return render(request, template_name, {'form':form})
@admin_required
def edit_lesson(request, pk):
	template_name = 'home/LessonForm.html'
	instance = Lessons.objects.get(pk = pk)
	form = EditLessonForm(instance=instance)
	if request.method == "POST":
		form = EditLessonForm(request.POST, request.FILES, instance = instance)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user.admin:
				form.save()
				return redirect('gym:main')
			else:
				return redirect('home:home')
		else:
			form = EditLessonForm(instance=instance)
	return render(request, template_name, {'form':form})

@login_required
def add_comment(request, pk):
	template_name = 'home/gym_detail.html'
	form = CommentForm()
	post = Lessons.objects.get(pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user:
				form.user=request.user
				form.pk_comment = post.pk
				form.gym = True
				form.save()
				return redirect('gym:expand', pk=pk)
			else:
				return redirect('home:home')
		else:
			form = CommentForm()
	return redirect('gym:expand', pk=pk)

@login_required
def add_reply(request, pk, post_pk):
	template_name = 'home/gym_detail.html'
	form = ReplyForm()
	comment = Comment.objects.get(pk = pk)
	if request.method == "POST":
		form = ReplyForm(request.POST)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user:
				form.comment = comment
				form.user=request.user
				form.save()
				return redirect('gym:expand', pk=post_pk)
			else:
				return redirect('home:home')
		else:
			form = ReplyForm()
	return redirect('gym:expand', pk=post_pk)
