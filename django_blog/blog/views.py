from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

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



