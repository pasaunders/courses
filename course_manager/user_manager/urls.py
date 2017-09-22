from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='user_display'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login, name='login'),
    url(r'^success/(?P<means>\w+)', views.success, name='success')
]