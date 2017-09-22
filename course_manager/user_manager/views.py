from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Users
from .forms import register_form, login_form
import bcrypt


def index(request):
    context = {
        'register_form': register_form,
        'login_form': login_form,
    }
    return render(reqeust, 'user_manager/index.html', context)


def register(request):
    if request.method == 'POST':
        errors = Users.objects.user_validator(request.POST)
        if errors:
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('users:user_display'))
        else:
            Users.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                password=bcrypt.hashpw(
                    request.POST['password'].encode(),
                    bcrypt.gensalt()
                    )
            )
            return redirect(reverse('users:success'))


def login(request):
    if request.method == 'POST':
        if bcrypt.checkpw(
            request.POST['password'].encode(),
            Users.objects.filter(email=request.POST['email'])['password']
            ):
            # TODO: set session and redirect to success, build success and index html.


def success(request):
    pass