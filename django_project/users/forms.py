from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):

   class Meta:
      model = User
      #fields = "__all__"
      fields =('username', 'email', 'first_name', 'last_name')


class UpdateForm(forms.ModelForm):

   class Meta:
      model = User
      
      fields =['email']
  
   