from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib.auth import login, get_user_model
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from accounts.forms import MyUserCreationForm
from django.core.paginator import Paginator
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from webapp.models import Post

User = get_user_model()


class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_page = self.request.GET.get('next')
        if not next_page:
            next_page = self.request.POST.get('next')
        if not next_page:
            next_page = reverse('webapp:home')

        return next_page

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(author=self.object).order_by('-created_at')
        return context