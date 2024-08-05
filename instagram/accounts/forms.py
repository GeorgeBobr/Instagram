from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar', 'password1', 'password2', 'first_name', 'last_name', 'bio', 'phone_number', 'gender']



