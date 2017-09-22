from django import forms


class register_form(forms.Form):
    name = forms.CharField(label='Name:', min_length=2, max_length=60)
    email = forms.EmailField(label='Email', unique=True)
    password = forms.CharField(label='Password:', min_length=8, widget='PasswordInput')
    confirm_password = forms.CharField(label='Confirm Password:')


class login_form(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password:')
