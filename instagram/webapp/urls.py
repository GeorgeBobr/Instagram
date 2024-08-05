from django.urls import path
from .views import HomeView, PostCreateView

app_name = 'webapp'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
]
