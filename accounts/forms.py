from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .validators import StandardPasswordValidator
from passagesharer.models import Passage

class SimpleRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].validators.append(StandardPasswordValidator()) # type: ignore
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

        if 'email' in self.fields:
            del self.fields['email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Passage
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class UsernameChangeForm(forms.Form):
    new_username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="New username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm password"
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UsernameChangeForm, self).__init__(*args, **kwargs)

    def clean_new_username(self):
        new_username = self.cleaned_data.get('new_username')

        if User.objects.filter(username=new_username).exclude(pk=self.user.pk).exists():
            raise forms.ValidationError("This username has been used.")
        
        return new_username

    def clean_password(self):
        password = self.cleaned_data.get('password')
    
        if not authenticate(username=self.user.username, password=password):
            raise forms.ValidationError("Your password is wrong.")
        
        return password