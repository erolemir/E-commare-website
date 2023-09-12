from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100)
    
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Kullanıcı Adı', max_length=30)
    email = forms.EmailField(label='Email')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        

