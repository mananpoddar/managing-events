from django import forms
from django.core import validators
from blog.models import input,UserProfileInfo,User




class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField()
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,)


class AuthorForm(forms.ModelForm):
 
    class Meta:
        model = input
        fields = "__all__"
        error_messages = {
            "time":{
                "unique":"hi there! it looks like there is some event on the same time ",
            }
        }

class Authentic(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =("username","password","first_name","last_name","email",)

class UserProfile(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ("picture",)
