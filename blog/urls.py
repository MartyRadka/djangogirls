from django.conf.urls import url
from . import views

urlpatterns = [
    # jmeno stranky z view
    url(r'blog', views.post_list, name='post_list'),
]

