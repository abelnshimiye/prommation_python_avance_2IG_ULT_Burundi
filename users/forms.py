from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext, gettext_lazy as _, pgettext

# from django.contrib.auth.handlers import UsernameField

from allauth.account.forms import LoginForm, ChangePasswordForm

from django import forms

from .models import User
from allauth.account.forms import SignupForm
# from allauth.account.forms import ChangePasswordForm


# class CustomUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#             super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#             self.fields['email'].required = True
            
#     class Meta (UserCreationForm.Meta):
#         model = get_user_model()
#         # model = CustomUser
#         fields = ('email', 'username','phone_number',)

class CustomUserCreationForm(SignupForm):
    phone_number = forms.CharField(max_length=50, required=True)
    username = forms.CharField(max_length=50, required=True)

    def save(self, request):
        # First let Allauth create the user
        user = super().save(request)

        # Add your extra custom fields
        user.phone_number = self.cleaned_data['phone_number']
        user.username = self.cleaned_data['username']

        user.save()
        return user
        

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        # model = CustomUser
        fields = ('email', 'username','phone_number',)




class LoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
            super(LoginForm, self).__init__(*args, **kwargs)
            self.fields['password'].required


class ChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
            super(ChangePasswordForm, self).__init__(*args, **kwargs)
            self.fields['password2'].label = "Password confirmation"
    
    





# class MyCustomChangePasswordForm(ChangePasswordForm):

#     def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             # here you can change the fields
#             self.fields['password2'] = forms.PasswordField(label='custom label')





# from allauth.account.forms import ChangePasswordForm
# class MyCustomChangePasswordForm(ChangePasswordForm):
#     def save(self):

#         # Ensure you call the parent class's save.
#         # .save() does not return anything
#         super(MyCustomChangePasswordForm, self).save()

#         # Add your own processing here.

# from allauth.account.forms import SignupForm
# from django import forms
# class CustomSignupForm(SignupForm):
#     first_name = forms.CharField(max_length=30, label='First Name')
#     last_name = forms.CharField(max_length=30, label='Last Name')
 
#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()
#         return user