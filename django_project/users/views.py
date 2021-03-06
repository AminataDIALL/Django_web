
import json

from django.shortcuts import render, redirect
from django.views.generic import UpdateView, ListView

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import User
from django.core import serializers
from django.views.generic import TemplateView, View
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404



from .forms import UpdateForm, UserCreationForm

def home_view(request):
    return render(request, 'users/home.html')


def register_view(request):
    register_form = UserCreationForm(request.POST or None)
    if request.method=="POST":
        register_form = UserCreationForm(request.POST or None)
          
        if register_form.is_valid():
            #cleaned_data => recuperation des unputs
            register_form.save()
            username = register_form.cleaned_data.get('username')
            
            messages.success(request, f'Hello {username}, ton compte est créer avec succèes')
            return redirect('login')
        else:
            form = UserCreationForm()
        
    return render(request, 'users/register.html', {'form' : register_form })
 
@login_required()
def profil_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
       
        u = User.objects.get(username=username)
        
        
    return render(request, 'users/index.html',{'user':u})


 
@login_required()
def liste_view(request):
    username = request.user.username

    return render(request, 'users/liste.html', {
        'user': User.objects.get(username=username),
    })



def edit_profil(request, pk):

    
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":

        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                "movieListChanged": None,
                "showMessage": f"{user.email} updated."
                })
                }
                )
    else:
        form = UpdateForm(instance=user)
    return render(request,'users/form-edit.html', {
        'form': form,
        'user': user,
    })

@require_POST
def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    #user.save()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "movieListChanged": None,
                "showMessage": f"{user.email} update."
            })
        })


# @login_required()
# def update_view(request):
#     update_form = UpdateForm(request.POST or None)
#     if request.method=="POST":
#         update_form = UpdateForm(request.POST or None)
#         email = request.POST['email']
#         print(email)
#         if request.user.is_authenticated:
#             username = request.user.username
#             u = User.objects.get(username=username)
#             u.email = email
#             u.save()
#             return redirect('profil')
            
#     else:
#         form = UpdateForm()  
#     return render(request, 'users/update.html', {'form' : update_form })