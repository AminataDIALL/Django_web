from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



from . import views

urlpatterns = [
    path('accounts/login/', admin.site.urls),
    path('home/',views.home_view,name='home'),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profil/',views.profil_view,name='profil'),
    path('update/',views.update_view,name='update'),
    
]
