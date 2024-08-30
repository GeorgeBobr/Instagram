from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts.views import RegisterView, UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='registration'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
]
