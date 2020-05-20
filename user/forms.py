from django import forms

from user.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ForgotForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

class EmailForm(forms.Form):
    email = forms.EmailField()




class RegForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {"username","first_name","last_name", "email", "password","profile_pic"}

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()

class EditForm(forms.Form):
    username = forms.CharField(required=False)
    email = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    profile_pic = forms.FileField(required=False)

