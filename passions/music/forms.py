from django.forms import ModelForm
from .models import Youtube

class LessonForm(ModelForm):
	class Meta:
		model = Youtube
		exclude = ['user', 'date']
	def __init__(self, *args, **kwargs):
		super(LessonForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['placeholder'] = 'Name of the lesson'
		self.fields['description'].widget.attrs['placeholder'] = 'description of the lesson'
		self.fields['url'].widget.attrs['placeholder'] = 'Any url to video(Youtube)'


class EditLessonForm(ModelForm):
	class Meta:
		model = Youtube
		exclude = ['user', 'date']