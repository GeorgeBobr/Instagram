from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from webapp.models import Post
from .forms import UserSearchForm

User = get_user_model()

class UserSearchView(ListView):
    model = User
    template_name = 'search/search.html'
    context_object_name = 'users'
    form_class = UserSearchForm

    def get_queryset(self):
        form = self.get_form()
        query = form.cleaned_data.get('query', '')

        if query:
            return User.objects.filter(
                username__icontains=query
                ) | User.objects.filter(
                    email__icontains=query
                ) | User.objects.filter(
                    first_name__icontains=query
                )
        return User.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
