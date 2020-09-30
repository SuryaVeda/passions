from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Profile
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class VisitorRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


    @transaction.atomic
    def save(self, commit=True):
        user = super(VisitorRegisterForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        user.outsider = True
        if commit:
           user.save()
        return user


class AdminRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


    @transaction.atomic
    def save(self, commit=True):
        user = super(AdminRegisterForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        user.admin = True
        user.staff = True
        user.is_active = True
        if commit:
           user.save()
        return user

class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    username = forms.CharField(max_length = 40)
    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            user.staff = True
            user.is_active = True
        return user
class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'admin', 'username')

    def clean_password(self):
        return self.initial["password"]


class ProfileForm(forms.ModelForm):
    dob = forms.DateField(input_formats=['%m/%d/%Y'], required = False, widget = forms.TextInput(attrs={
        'id': 'datepicker-4'}))

    class Meta:
        model = Profile
        fields = [ 'dob', 'links', 'phone']
