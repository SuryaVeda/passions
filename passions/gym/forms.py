from django.forms import ModelForm
from .models import Lessons

class LessonForm(ModelForm):
	class Meta:
		model = Lessons
		exclude = ['user', 'date']
	def __init__(self, *args, **kwargs):
		super(LessonForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['placeholder'] = 'Name of the lesson'
		self.fields['description'].widget.attrs['strip'] = False
		self.fields['description2'].widget.attrs['strip'] = False

		self.fields['description3'].widget.attrs['strip'] = False
		self.fields['description4'].widget.attrs['strip'] = False
		self.fields['description'].widget.attrs['placeholder'] = 'para one of the lesson, (optional)'
		self.fields['description2'].widget.attrs['placeholder'] = 'para one of the lesson, (optional)'
		self.fields['description3'].widget.attrs['placeholder'] = 'para one of the lesson, (optional)'
		self.fields['description4'].widget.attrs['placeholder'] = 'para one of the lesson, (optional)'

		self.fields['url'].widget.attrs['placeholder'] = 'Any url to video(Youtube)'


class EditLessonForm(ModelForm):
	class Meta:
		model = Lessons
		exclude = ['user', 'date']