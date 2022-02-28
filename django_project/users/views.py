from django.shortcuts import render, redirect


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import User
from django.core import serializers
from django.views.generic import TemplateView, View



from .forms import UpdateForm

def home_view(request):
    return render(request, 'users/home.html')


@login_required()
def profil_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        print(username)
        u = User.objects.get(username=username)
        
        
    return render(request, 'users/profil.html',{'user':u})



@login_required()
def update_view(request):
    update_form = UpdateForm(request.POST or None)
    if request.method=="POST":
        update_form = UpdateForm(request.POST or None)
        email = request.POST['email']
        if request.user.is_authenticated:
            username = request.user.username
            u = User.objects.get(username=username)
            u.email = email
            u.save()
            return redirect('profil')
            
    else:
        form = UpdateForm()  
    return render(request, 'users/update.html', {'form' : update_form })
 
@login_required()
def liste_view(request):
    
    if request.user.is_authenticated:
            
        liste = User.objects.all()
          
            
  
    return render(request, 'users/update.html', {'liste' : liste })
 

    

