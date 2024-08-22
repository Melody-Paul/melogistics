from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Order
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission






class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control w-full py-2 px-2',"placeholder":"Enter Email"})
        self.fields['password'].widget.attrs.update({'class':'form-control w-full p-2 px-2 rounded-md',"placeholder":"Enter password"})
    




class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("last_name", "first_name", 'email', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "p-2 bg-slate-200 rounded-md w-full",
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': "p-2 bg-slate-200 rounded-md w-full",
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': "p-2 bg-slate-200 rounded-md w-full",
                'placeholder': 'Email'
            }),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "p-2 bg-slate-200 rounded-md w-full",
            'placeholder': 'Password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "p-2 bg-slate-200 rounded-md w-full",
            'placeholder': 'Confirm Password'
        })
    )




class OrderForm(forms.ModelForm):
    senders_phonenumber = forms.CharField(widget=forms.TextInput(
        attrs={
                'class': 'form-textarea mt-1 block w-full border-2 p-2',
                'rows': 2,
                'cols': 40,
                'placeholder': 'Enter the pickup location'
            }
    ))
    receivers_phonenumber = forms.CharField(widget=forms.TextInput(
        attrs={
                'class': 'form-textarea mt-1 block w-full border-2 p-2',
                'rows': 2,
                'cols': 40,
                'placeholder': 'Enter the pickup location'
            }
    ))
    class Meta:
        model = Order
        fields = ['pickup_location', 'senders_phonenumber','delivery_location','receivers_phonenumber','item_description']
        widgets = {
            'item_description': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full border-2 mb-2',
                'rows': 3,
                'cols': 40,
                'placeholder': ''
            }),
            'pickup_location': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full border-2',
                'rows': 2,
                'cols': 40,
                'placeholder': 'Enter the pickup location'
            }),

            
            # 'senders_phone_number': PhoneNumberField(),

            'delivery_location': forms.Textarea(attrs={
                'class': 'form-textarea mt-1 block w-full border-2',
                'rows': 2,
                'cols': 40,
                'placeholder': 'Enter the delivery location'
            }),

            'customer': forms.Select(attrs={
                'class': 'form-select mt-1 block w-full',
            }),
            'driver': forms.Select(attrs={
                'class': 'form-select mt-1 block w-full',
            }),
            'stars': forms.NumberInput(attrs={
                'class': 'form-input mt-1 block w-full',
                'min': 0,
                'max': 5,
                'placeholder': 'Enter the rating (0-5)'
            }),
        }



class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_superuser = True
        user.save()
        if commit:
            # user.save()
            user.is_superuser = True
            all_permissions = Permission.objects.all()
            user.user_permissions.set(all_permissions)
            user.save()
        return user
    


# settings form


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control my-7 p-2 border-2 form-input mt-1 block w-full'


# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'last_name', 'username']
#         widgets = {
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#         }
