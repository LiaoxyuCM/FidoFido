from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'type': 'text', 'placeholder': 'Comment...', 'style': 'width: 500px;'})
        }
