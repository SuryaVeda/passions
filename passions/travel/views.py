from django.shortcuts import render, redirect
from .models import Travel
from .forms import LessonForm, EditLessonForm
from django.contrib.auth.decorators import login_required
import facebook
from home.decorators import admin_required
from home.models import Comment, Reply
from home.forms import CommentForm, ReplyForm

# Create your views here.
graph = facebook.GraphAPI(access_token="EAAHlA6rZAYkgBAAPwZBmWd8xzhA1AjTOhtRMZCAP95K5p0f7IanZA0PzjZCR2ec2ArhRUwq2GzMQlDzlj9FmsRRKFtl4SItLmXBzqGlRCt4XRKxauOqU4HhLtFAsZCdKG6xZBnkh4jDg3D2tSkVcLdt0EiHUMfsvetAX2C6hi9DKQZDZD", version="3.1")
page_id = '102395031101655'

def travel(request):
	template_name = 'home/travel.html'
	posts = Travel.objects.order_by('pk')
	context = {'posts':posts}
	return render(request, template_name, context)
def details(request, pk):
	template_name = 'home/travel_detail.html'
	posts = Travel.objects.order_by('pk')
	form = CommentForm()
	replyForm = ReplyForm()
	comments = Comment.objects.filter(travel=True, pk_comment=pk)
	comment_length = len(comments)
	replies = Reply.objects.order_by('pk')
	stor = Travel.objects.get(pk=pk)
	context = {'stor':stor, 'posts':posts, 'form':form, 'replyForm':replyForm, 'comments':comments, 'replies':replies, 'comment_length':comment_length}
	return render(request, template_name, context)
@login_required
@admin_required
def add_lesson(request):
	template_name = 'home/TravelForm.html'
	form = LessonForm()
	if request.method == "POST":
		form = LessonForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.cleaned_data['name']
			why= form.cleaned_data['why']
			form = form.save(commit = False)
			if request.user:
				form.user=request.user
				form.save()
				post = Travel.objects.get(name= name, why= why)
				post_url = 'https://mypassions.site/travel/'
				image_url = '/home/surya/passions/passions' + post.img1.url
				graph.put_photo(image=open(image_url, 'rb'), message = post.name + '.      Check out the url for complete article.' + post_url )
				return redirect('travel:main')
			else:
				return redirect('home:home')
		else:
			form = LessonForm()
	return render(request, template_name, {'form':form})
@login_required
@admin_required
def edit_lesson(request, pk):
	template_name = 'home/editTravelForm.html'
	instance = Travel.objects.get(pk = pk)
	form = EditLessonForm(instance=instance)
	if request.method == "POST":
		form = EditLessonForm(request.POST, request.FILES, instance = instance)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user:
				form.save()
				return redirect('travel:main')
			else:
				return redirect('home:home')
		else:
			form = EditLessonForm(instance=instance)
	return render(request, template_name, {'form':form})


@login_required
def add_comment(request, pk):
	template_name = 'home/travel_detail.html'
	form = CommentForm()
	post = Travel.objects.get(pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user:
				form.user=request.user
				form.pk_comment = post.pk
				form.travel = True
				form.save()
				return redirect('travel:expand', pk=pk)
			else:
				return redirect('home:home')
		else:
			form = CommentForm()
	return redirect('travel:expand', pk=pk)

@login_required
def add_reply(request, pk, post_pk):
	template_name = 'home/travel_detail.html'
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
				return redirect('travel:expand', pk=post_pk)
			else:
				return redirect('home:home')
		else:
			form = ReplyForm()
	return redirect('travel:expand', pk=post_pk)