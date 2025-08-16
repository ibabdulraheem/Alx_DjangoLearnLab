# Creating CUSTOM REGISTRATION FORM and extend UserCreationForm to add the email field.
from django import forms
from .models import Post,Comment
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
  email = forms.EmailField(required=True)
  
  class meta(UserCreationForm.Meta):
    fields = UserCreationForm.Meta.fields + ('email',)


class PostForm(forms.ModelForm):
  class meta:
    model = Post
    fields = ['title','content','tags']
    widgets = {
       'tags': TagWidget(),
    }

    
# CREATING COMMENT FORM TO BE USED IN THE COMMENT VIEWS
# ["CommentForm(forms.ModelForm)", "model = Comment"]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']   # Only allow editing the text of a comment
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your comment here...',
                'rows': 4
            }),
        }
        labels = {
            'text': 'Your Comment',
        }

    # Custom validation
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text.strip()) < 5:
            raise forms.ValidationError("Comment must be at least 5 characters long.")
        return text



