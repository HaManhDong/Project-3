

from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^/$',views.UserView.index,name='index'),
    url(r'^registry/$',views.UserView.post_registry,name='post_registry_user')
]