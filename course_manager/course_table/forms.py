from django import forms


class add_course_form(form.Forms):
    name = forms.CharField(label='Name:', min_length=5, max_length=60)
    description = forms.CharField(label='Description:', min_length=15, max_length=500, widget=forms.Textarea)
