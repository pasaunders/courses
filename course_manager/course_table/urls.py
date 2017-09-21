from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'add', views.add_course, name='add_course'),
    url(r'courses/destroy/(?P<user_id>[0-9]+)', views.delete, name='course_delete'),
    url(r'delete/(?P<user_id>[0-9]+)', views.remove, name='course_final_remove'),
    url(r'$', views.display, name='course_display'),
]