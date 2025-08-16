from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required



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
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'



# view that handles FORM submission
@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect ('post_detail',pk = post.pk)
        else:
            form = PostForm()
        return render (request,'blog/create_post.html',{'form':form})

@login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/update_post.html', {'form': form})
    
# CREATING VIEWS FOR A COMMENT_FORM CREATED INITIALLY IN THE forms.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })
   



