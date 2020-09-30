from django.shortcuts import render, redirect
from .models import Youtube
from urllib.parse import urlparse, parse_qs
from .forms import LessonForm, EditLessonForm
from home.decorators import admin_required
# Create your views here.
def music(request):
	template_name = 'home/music.html'
	videos = Youtube.objects.order_by('pk')   
	return render(request, template_name, {'videos':videos})

def details(request, pk):
	template_name = 'home/music_detail.html'
	lessons = Youtube.objects.order_by('pk')
	post = Youtube.objects.get(pk=pk)
	context = {'post':post, 'lessons':lessons}
	return render(request, template_name, context) 
@admin_required
def add_lesson(request):
	template_name = 'home/lessonForm.html'
	form = LessonForm()
	if request.method == "POST":
		form = LessonForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user:
				form.user=request.user
				form.save()
				return redirect('music:main')
			else:
				return redirect('home:home')
		else:
			form = LessonForm()
	return render(request, template_name, {'form':form})
@admin_required
def edit_lesson(request, pk):
	template_name = 'home/editLessonForm.html'
	instance = Youtube.objects.get(pk = pk)
	form = EditLessonForm(instance=instance)
	if request.method == "POST":
		form = EditLessonForm(request.POST, request.FILES, instance = instance)
		if form.is_valid():
			form = form.save(commit = False)
			if request.user:
				form.user=request.user
				form.save()
				return redirect('music:main')
			else:
				return redirect('home:home')
		else:
			form = EditLessonForm(instance=instance)
	return render(request, template_name, {'form':form})


		
