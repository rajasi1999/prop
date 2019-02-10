from django import forms
from .models import Student, College
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Student
        fields = ('email', 'college_name',)

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ('name','college_address','college_code')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password','email')
