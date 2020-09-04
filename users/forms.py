from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address_line1','address_line2','pincode','contactno',"image"]
