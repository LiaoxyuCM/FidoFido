from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .validators import StandardPasswordValidator
from passagesharer.models import Passage

class SimpleRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].validators.append(StandardPasswordValidator()) # type: ignore
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address has been used.")
        return email

class PostForm(forms.ModelForm):
    class Meta:
        model = Passage
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Content'}),
        }

class UsernameChangeForm(forms.Form):
    new_username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "New username"}),
        label="New username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirm password"}),
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
    
class SMSCodeForm(forms.Form):
    # Send sms-code to user's email address
    sms_code = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "SMS code"}),
        label="SMS code"
    )