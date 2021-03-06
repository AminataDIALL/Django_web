from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



from . import views

urlpatterns = [
    #path('accounts/login/', admin.site.urls),
    path('',views.home_view,name='home'),
    path('register/',views.register_view,name='register'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profil',views.profil_view, name="profil"),
    path('liste/',views.liste_view,name='liste'),
    path('user/<int:pk>/edit/', views.edit_profil, name='edit_user'),
    path('user/<int:pk>/update/', views.update_user, name='update_user'),
    

    
]
