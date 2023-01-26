from django.urls import path

from . import views

app_name = 'crm'
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('profile/', views.ProfileView, name='profile'),
    path('upload/', views.upload_file, name='upload'),
    path('send/', views.send_email, name='send_mail')
]
