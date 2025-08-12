from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post



# Create your views here.
# Creating view that uses the form we created initially in the forms.py
# It will handle both GET request (display the form) and the POST request (process form submission)

def register(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form':form})

# View to display a list of all blog posts
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

# view to display detail of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

# view to create a new blog post (require a user to login first)
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title','content']
# Override form_valid method to set the author to the current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# View to update an existing blog post which requires the user loggind first
class PostUpdateView(UpdateView):
    model = Post
    
    



