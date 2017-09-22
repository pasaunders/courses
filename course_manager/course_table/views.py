from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Courses
from .forms import add_course_form


def display(request):
    """Show all courses, and form for adding new ones."""
    context = {
        'courses': Courses.objects.all(),
        'form': add_course_form(),
    }
    return render(request, 'course_table/index.html', context)


def delete(request, user_id):
    """Show 'are you sure' page for deleting courses."""
    context = {
        'course': Courses.objects.get(id=user_id),
        'id': user_id,
    }
    return render(request, 'course_table/delete.html', context)


def remove(request, user_id):
    """Permanently remove selected course."""
    Courses.objects.get(id=user_id).delete()
    return redirect(reverse('courses:course_display'))


def add_course(request):
    """Add course."""
    if request.method == "POST":
        Courses.objects.create(
            name=request.POST['name'],
            desc=request.POST['desc']
        )
    return redirect(reverse('courses:course_display'))