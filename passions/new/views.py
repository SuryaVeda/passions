from django.shortcuts import render, redirect
from .models import Book, Page
from .forms import BookForm, PageForm
import json, requests, facebook
from urllib.parse import urljoin
from django.conf import settings
from django.views.generic import DetailView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from home.decorators import admin_required
from home.models import Comment, Reply
from home.forms import CommentForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
# Create your views here.
graph = facebook.GraphAPI(access_token="EAAHlA6rZAYkgBAAPwZBmWd8xzhA1AjTOhtRMZCAP95K5p0f7IanZA0PzjZCR2ec2ArhRUwq2GzMQlDzlj9FmsRRKFtl4SItLmXBzqGlRCt4XRKxauOqU4HhLtFAsZCdKG6xZBnkh4jDg3D2tSkVcLdt0EiHUMfsvetAX2C6hi9DKQZDZD", version="3.1")
page_id = '102395031101655'

def library(request):
	template_name = "new/page.html"
	books = Book.objects.order_by('pk')
	form = CommentForm()
	replyForm = ReplyForm()
	comments = Comment.objects.filter(stories=True)
	replies = Reply.objects.order_by('pk')
	comment_length = len(comments)
	context = {'books':books, 'form':form, 'replyForm':replyForm, 'comments':comments, 'replies':replies,  'comment_length':comment_length}
	return render(request, template_name, context)

@admin_required
def create_book(request):
	template_name = "new/form.html"
	form = BookForm()
	if request.method =='POST':
		if len(request.POST['author']) > 1:
			author = request.POST.getlist('author')
			a = json.dumps(author)
			form = BookForm(request.POST, request.FILES)
			if form.is_valid():
				name = form.cleaned_data['name']
				summary = form.cleaned_data['summary']
				form = form.save(commit=False)
				form.author= a
				form.draft = True
				form.save()
				return redirect('new:lib')
			else:
				form = BookForm()
		else:
			form = BookForm(request.POST)
			author = request.POST['author']
			if form.is_valid():
				form = form.save(commit=False)
				form.author = author
				form.save()
				return redirect('new:lib')
			else:
				form = BookForm()		
	return render(request, template_name, {'form':form})

@admin_required
def details(request, pk):
	template_name = 'new/details.html'
	book = Book.objects.get(pk = pk)
	pages = Page.objects.filter(book = book).order_by('-pk').reverse()
	context = {'book':book, 'pages':pages}
	return render(request, template_name, context)
@admin_required
def drafts(request):
	template_name = 'new/drafts.html'
	books = Book.objects.filter(draft = True)
	context = {'books':books}
	return render(request, template_name, context)
@admin_required
def save_draft(request, pk):
	book = Book.objects.get(pk = pk)
	book.draft = True
	book.save()
	return redirect('new:draf')
@admin_required
def save_book(request, pk):
	book = Book.objects.get(pk = pk)
	book.draft = False
	book.save()
	post = book
	post_url = 'https://mypassions.site/library/'
	image_url = '/home/surya/passions/passions' + post.image.url
	graph.put_photo(image=open(image_url, 'rb'), message = post.name + '.           ' +post.summary + '.      Check out the url for complete article.' + post_url )
	return redirect('new:lib')
@admin_required
def create_page(request, pk):
	template_name = "new/detailsForm.html"
	form = PageForm()
	book = Book.objects.get(pk = pk)
	if request.method =='POST':
		form = PageForm(request.POST)
		if form.is_valid():
			length = len(form.cleaned_data.get('para'))
			if length > 1050:
				paraOne = form.cleaned_data.get('para')[slice(0, 1050)]
				paraTwo = form.cleaned_data.get('para')[slice(1050, length)]
				form = form.save(commit = False)
				form.book = book
				form.para = paraOne
				form.save()
				page = Page.objects.create(heading = "", para = paraTwo, book = book)
				page.save()
				return redirect('new:bookDetails', pk = pk )

			elif length < 1050:
				form = form.save(commit = False)
				form.book = book
				form.save()
				return redirect('new:bookDetails', pk = pk )
		else:
			form = PageForm()
	else:
		form = PageForm()

	return render(request, template_name, {'form':form})
@admin_required
def edit_page(request, pk):
	template_name = 'new/editForm.html'
	instance = Page.objects.get(pk=pk)
	form = PageForm(instance=instance)
	page = Page.objects.get(pk=pk)
	id = instance.book.pk
	book = Book.objects.get(pk=id)
	if request.method =='POST':
		form = PageForm(request.POST, instance=instance)
		if form.is_valid():
			length = len(form.cleaned_data.get('para'))
			if length > 1050:
				paraOne = form.cleaned_data.get('para')[slice(0, 1050)]
				paraTwo = form.cleaned_data.get('para')[slice(1050, length)]
				form = form.save(commit = False)
				form.book = book
				form.para = paraOne
				form.save()
				left = book.get_pages() - pk
				pageList = list(range(1, left+1))
				for n in pageList:
					nextPage = Page.objects.get(pk = pk + n)
					if nextPage:
						b = Page.objects.get(pk = pk+n)
						b.para = paraTwo + b.para
						length = len(b.para)
						if length > 1050:
							paraOne = b.para[slice(0, 1050)]
							paraTwo = b.para[slice(1050, length)]
							b.para = paraOne
							b.save()
						else:
							b.save()
							return redirect('new:bookDetails', pk = id )
							break			
					else:
						page = Page.objects.create(heading="", para= paraTwo, book= book)
						page.save()
						return redirect('new:bookDetails', pk = id )
						break
				else:
					page = Page.objects.create(heading="", para= paraTwo, book= book)
					page.save()
					return redirect('new:bookDetails', pk = id )
			elif length < 1050:
				form_para = form.cleaned_data.get('para')
				form.save(commit=False)
				form.para = form_para
				form.book = book
				form.save()
				left = book.get_pages() - pk
				pageList = list(range(1, left+1))
				for n in pageList:
					nextPage = Page.objects.get(pk = pk+n)
					if nextPage:
						a = Page.objects.get(pk = pk+n-1)
						b = Page.objects.get(pk = pk+n)
						length = len(a.para)
						if b.para == None:
							return redirect('new:bookDetails', pk = id )
						bLength = len(b.para)
						remainderLength = 1050 - length
						if bLength >= remainderLength:
						    remainder = b.para[slice(0, remainderLength)]
						    newBPara = b.para[slice(remainderLength, bLength)]
						    b.para = newBPara
						    b.save()
						    newPara = form_para + remainder
						    a.para = newPara
						    a.save()
						else:
							newPara = a.para + b.para
							newBPara = ""
							b.para = newBPara
							b.save()
							a.para = newPara
							a.save()
							
					else:
						return redirect('new:bookDetails', pk = id )
						break
				else:
					return redirect('new:bookDetails', pk = id )			
		else:
			form = PageForm(instance=instance)
	else:
	    form = PageForm(instance=instance)
	return render(request, template_name, {'form':form, 'instance':instance})



def save_pdf(request, pk):
	book = Book.objects.get(pk = pk)
	pages = Page.objects.filter(book = book)
	context = {'book':book, 'pages':pages}
	html_string = render_to_string('new/details.html', context)
	html = HTML(string=html_string)
	html.write_pdf(target='/tmp/myStories.pdf', stylesheets=[CSS(settings.STATIC_ROOT + '/new/details.css')]);

	fs = FileSystemStorage('/tmp')
	with fs.open('myStories.pdf') as pdf:
		response = HttpResponse(pdf, content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="myStories.pdf"'
		return response

	return response


def overview(request, pk ):
	template_name = 'new/overview.html'
	book = Book.objects.get(pk = pk)
	pages = Page.objects.filter(book = book).order_by('-pk').reverse()
	context = {'book':book, 'pages':pages}
	return render(request, template_name, context)

@login_required
def add_comment(request, pk):
	template_name = 'home/page.html'
	form = CommentForm()
	post = Book.objects.get(pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user:
				form.user=request.user
				form.pk_comment = post.pk
				form.stories = True
				form.save()
				return redirect('new:lib')
			else:
				return redirect('home:home')
		else:
			form = CommentForm()
	return redirect('new:lib')

@login_required
def add_reply(request, pk, post_pk):
	template_name = 'home/page.html'
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
				return redirect('new:lib')
			else:
				return redirect('home:home')
		else:
			form = ReplyForm()
	return redirect('new:lib')

