from django import forms
from .models import Book, Page

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = ['author']
class PageForm(forms.ModelForm):
	heading = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Heading'}))
	para = forms.CharField(required=True,strip=False, widget=forms.Textarea(attrs={'cols': 10, 'rows': 20}))
	def __init__(self, *args, **kwargs):
		super(PageForm, self).__init__(*args, **kwargs)
		self.fields['heading'].strip = False
		self.fields['para'].strip = False
		self.fields['para'].widget.attrs['placeholder'] = 'Text'
	class Meta:
		model = Page
		fields = ['para', 'heading']

