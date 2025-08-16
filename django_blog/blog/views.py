from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.db import models
from django.db.models import Q




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
   
# Comment views

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        # attach post and user automatically
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # redirect back to the post detail page
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "comment_form.html"

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comment_confirm_delete.html"

    def test_func(self):
        # Only comment author can delete
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post.pk})



#  ["CommentCreateView", "CommentUpdateView", "CommentDeleteView"]

# Creating a search view using Q objects:
from django.db.models import Q
from django.shortcuts import render
from .models import Post


# ["Post.objects.filter", "title__icontains", "tags__name__icontains", "content__icontains"]
def post_search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/post_search.html', {'query': query, 'results': results})

