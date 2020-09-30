from django.forms import ModelForm
from .models import Travel

class LessonForm(ModelForm):
	class Meta:
		model = Travel
		exclude = ['user', 'date']
	def __init__(self, *args, **kwargs):
		super(LessonForm, self).__init__(*args, **kwargs)
		self.fields['why'].strip = False
		self.fields['fun'].strip = False
		self.fields['how'].strip = False
		self.fields['name'].widget.attrs['placeholder'] = 'Name of the trip'
		self.fields['why'].widget.attrs['placeholder'] = 'why this trip?'
		self.fields['fun'].widget.attrs['placeholder'] = 'Fun things to do'
		self.fields['how'].widget.attrs['placeholder'] = 'How to reach and stay?'
		self.fields['links'].widget.attrs['placeholder'] = 'Any links for further info'


class EditLessonForm(ModelForm):
	class Meta:
		model = Travel
		exclude = ['user', 'date']
	def __init__(self, *args, **kwargs):
		super(EditLessonForm, self).__init__(*args, **kwargs)
		self.fields['why'].strip = False
		self.fields['fun'].strip = False
		self.fields['how'].strip = False
		self.fields['name'].widget.attrs['placeholder'] = 'Name of the trip'
		self.fields['why'].widget.attrs['placeholder'] = 'why this trip?'
		self.fields['fun'].widget.attrs['placeholder'] = 'Fun things to do'
		self.fields['how'].widget.attrs['placeholder'] = 'How to reach and stay?'
		self.fields['links'].widget.attrs['placeholder'] = 'Any links for further info'


