from django import forms
from django.contrib.auth.forms import UserChangeForm
from home.models import UserProfile
from django.contrib.auth.models import User



class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email')
        wigdets = {
            'first_name':forms.TextInput(attrs={'class':'input','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'input','placeholder':'Last Name'}),
            'username':forms.TextInput(attrs={'class':'input','placeholder':'Username'}),
            'email':forms.TextInput(attrs={'class':'input','placeholder':'Email'}),
        }
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','address','city','country','image') 
        wigdets = {
            'phone':forms.TextInput(attrs={'class':'input','placeholder':'Phone'}),
            'address':forms.TextInput(attrs={'class':'input','placeholder':'Address'}),
            'city':forms.TextInput(attrs={'class':'input','placeholder':'City'}),
            'country':forms.TextInput(attrs={'class':'input','placeholder':'Country'}),
            'image':forms.FileInput(attrs={'class':'input','placeholder':'Image'}),
        }