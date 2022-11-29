from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import userInfo
# from django.https import http

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username'}),max_length=20)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))

    def clean(self,*args,**kwargs):
        username_ = self.cleaned_data.get("username")
        password_ = self.cleaned_data.get("password")

        if username_ and password_:
            user_ = userInfo.objects.filter(username__exact=username_)
            print(user_)
            if not user_:
                raise forms.ValidationError("Username does not exist.")
            elif(user_[0].password != password_):
                raise forms.ValidationError("Password doesn't match.")
            else:
                user_[0].is_login=True
                user_[0].save()
        return super(LoginForm,self).clean(*args,**kwargs)

class RegistrationForm(forms.Form):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=[('0','Male'),('1','Female')])
    email_id=forms.EmailField()
    username=forms.CharField(max_length=10)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput,help_text="Provide the same password again.")

    def clean(self,*args,**kwargs):
        p1 = self.cleaned_data['password']
        p2 = self.cleaned_data['confirm_password']

        if(p1!=p2):
            raise forms.ValidationError("Both Password are not matching.")
        return super(RegistrationForm,self).clean(*args,**kwargs)