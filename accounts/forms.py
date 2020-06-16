from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django import forms
from .models import User, UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
                            widget=forms.EmailInput(attrs={'class': 'form-control'}),
                            max_length=64, 
                            help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
                            ) 
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.is_staff = True
            user.save()
        return user


class ChangePasswordForm(forms.Form):
    
    password1 = forms.CharField(
                    label='<h5>New Password</h5>',
                    required=False,
                    widget=forms.PasswordInput(
                             attrs={
                             'class': 'form-control',
                             'placeholder': 'New Password'
                             }
                         ))
    password2 = forms.CharField(
                label='<h5>New Password</h5>',
                required=False,
                widget=forms.PasswordInput(
                         attrs={
                         'class': 'form-control',
                         'placeholder': 'Confirm New Password'
                         }
                     ))

class DeleteAccountPasswordForm(forms.Form):
    
    password = forms.CharField(
                     label='<h5>Confirm Password</h5>',
                    required=False,
                    widget=forms.PasswordInput(
                             attrs={
                             'class': 'form-control',
                             'placeholder': 'New Password'
                             }
                         ))


class UserUpdateForm(forms.Form):
    first_name = forms.CharField(
                        label='First Name',
                        required=False,
                        widget=forms.TextInput(
                        attrs={'class': 'form-control',
                                'placeholder': 'Enter your first name'
                                }
                            ),
                        )
    last_name = forms.CharField(
                        label='Last Name',
                        required=False,
                        widget=forms.TextInput(
                        attrs={'class': 'form-control',
                                'placeholder': 'Enter your last name'
                                }
                            ),
                        )
    email = forms.CharField(
                        label='E-mail',
                        required=False,
                        widget=forms.EmailInput(
                        attrs={'readonly':'readonly',
                                'class': 'form-control',
                                'placeholder': 'Enter your email'
                                }
                            ),
                        )

class UserProfileUpdateForm(forms.ModelForm):
   
    class Meta:
        model = UserProfile
        fields = [
            'profile_image',
            ]


