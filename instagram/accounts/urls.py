from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts.views import RegisterView, UserProfileView

app_name = 'accounts'

urlpatterns = [
    path('', LoginView.as_view(template_name="register/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='registration'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    # path('<int:pk>/profile/edit/', UserChangeView.as_view(), name='profile_change'),
    # path('<int:pk>/profile/password-change/', UserPasswordChangeView.as_view(), name='password_change'),
]
