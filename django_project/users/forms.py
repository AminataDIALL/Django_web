from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):

   class Meta:
      model = User
      fields = '__all__'

class UpdateForm(forms.Form):
   email = forms.EmailField(widget=forms.EmailInput(attrs={
       'class': 'form-control',
       'id' : 'form_email',
       'placeholder' : 'Your email '}))