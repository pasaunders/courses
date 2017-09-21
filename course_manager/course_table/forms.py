from django import forms


class add_course_form(forms.Form):
    name = forms.CharField(label='Name:', min_length=5, max_length=60)
    desc = forms.CharField(label='Description:', min_length=15, max_length=500, widget=forms.Textarea)
