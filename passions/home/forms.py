from django import forms
from .models import News, Category, Comment, Reply

class LessonForm(forms.ModelForm):
	class Meta:
		model = News
		exclude = ['user', 'date']
	def __init__(self, *args, **kwargs):
		super(LessonForm, self).__init__(*args, **kwargs)
		self.fields['heading'].widget.attrs['placeholder'] = 'heading of news'
		self.fields['description'].widget.attrs['placeholder'] = 'description of the news'
		self.fields['description'].widget.attrs['strip'] = False
		self.fields['url'].widget.attrs['placeholder'] = 'Any url to video(Youtube)'
		self.fields['url2'].widget.attrs['placeholder'] = 'Any url to other source!'
		self.fields['category'].widget.attrs['placeholder'] = 'Category'

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['description']
	def __init__(self, *args, **kwargs):
		super(CommentForm, self).__init__(*args, **kwargs)
		self.fields['description'].widget.attrs['placeholder'] = 'Add a comment...'

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ['description']
	def __init__(self, *args, **kwargs):
		super(ReplyForm, self).__init__(*args, **kwargs)
		self.fields['description'].widget.attrs['placeholder'] = 'Reply to the comment..'
