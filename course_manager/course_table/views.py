from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Courses
from .forms import add_course_form


def display(request):
    context = {
        'courses': Courses.objects.all()
    }
    return render(request, 'course_table/index.html', context)


def delete(request, user_id):
    context = {
        'course': Courses.objects.get(id=user_id)
    }
    return render(request, 'course_table/delete.html', context)