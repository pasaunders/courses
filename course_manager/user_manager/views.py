from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Users
from .forms import register_form, login_form
import bcrypt


def index(request):
    context = {
        'register_form': register_form(),
        'login_form': login_form(),
    }
    return render(request, 'user_manager/index.html', context)


def register(request):
    if request.method == 'POST':
        errors = Users.objects.user_validator(request.POST)
        if errors:
            for tag, error in errors.items():
                messages.error(request, error, extra_tags=tag)
                # TODO: Make sure flash messages work.
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
            return redirect(reverse('users:success', kwargs={'means': 'registered'}))
    return redirect(reverse('users:user_display'))


def login(request):
    if request.method == 'POST':
        user = Users.objects.filter(email=request.POST['email']).first()
        import pdb; pdb.set_trace()
        if bcrypt.checkpw(
            request.POST['password'].encode(),
            user.password.encode()
            ):
            request.session['id'] = user.id
            return redirect(reverse('users:success', kwargs={'means': 'loggedin'}))
    return redirect(reverse('users:user_display'))
            # TODO: set session and redirect to success, build success and index html.


def success(request, means):
    context = {
        'name': Users.objects.get(id=request.session['id']).name,
        'arrival': means,
    }
    return render(request, 'user_manager/success.html', context)