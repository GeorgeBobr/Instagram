from django.core.paginator import Paginator
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm

def home(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'posts': page_obj.object_list, 'page_obj': page_obj})

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return redirect('webapp:home')


