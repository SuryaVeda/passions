from django.shortcuts import render, redirect
from home.models import News
import facebook
from home.models import Comment, Reply
from home.forms import CommentForm, ReplyForm
from django.contrib.auth.decorators import login_required
# Create your views here.

graph = facebook.GraphAPI(access_token="EAAHlA6rZAYkgBAAPwZBmWd8xzhA1AjTOhtRMZCAP95K5p0f7IanZA0PzjZCR2ec2ArhRUwq2GzMQlDzlj9FmsRRKFtl4SItLmXBzqGlRCt4XRKxauOqU4HhLtFAsZCdKG6xZBnkh4jDg3D2tSkVcLdt0EiHUMfsvetAX2C6hi9DKQZDZD", version="3.1")
page_id = '102395031101655'


def stories(request):
	template_name = 'home/stories.html'
	news = News.objects.all().order_by('-date')
	form = CommentForm()
	replyForm = ReplyForm()
	comments = Comment.objects.filter(news=True)
	replies = Reply.objects.order_by('pk')
	comment_length = len(comments)
	context = {'news':news,  'form':form, 'replyForm':replyForm, 'comments':comments, 'replies':replies,  'comment_length':comment_length}
	return render(request, template_name, context)

def details(request, pk):
	template_name = 'home/stories_details.html'
	lessons = Stories.objects.order_by('pk')
	post = Stories.objects.get(pk=pk)
	context = {'post':post, 'lessons':lessons}
	return render(request, template_name, context) 

@login_required
def add_comment(request, pk):
	template_name = 'home/stories.html'
	form = CommentForm()
	post = News.objects.get(pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user:
				form.user=request.user
				form.pk_comment = post.pk
				form.news = True
				form.save()
				return redirect('stories:main')
			else:
				return redirect('home:home')
		else:
			form = CommentForm()
	return redirect('stories:main')

@login_required
def add_reply(request, pk, post_pk):
	template_name = 'home/stories.html'
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
				return redirect('stories:main')
			else:
				return redirect('home:home')
		else:
			form = ReplyForm()
	return redirect('stories:main')

