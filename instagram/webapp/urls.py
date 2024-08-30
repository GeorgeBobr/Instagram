from django.urls import path
from webapp import views

app_name = 'webapp'

urlpatterns = [
    path('home/', views.home, name='home'),
]
