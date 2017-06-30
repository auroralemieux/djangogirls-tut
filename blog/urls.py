from django.conf.urls import url
from . import views

urlpatterns = [
    # this is setting the root route
    url(r'^$', views.post_list, name='post_list'),
    
]
