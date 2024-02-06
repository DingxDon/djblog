from django.urls import path
from .views import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
]
