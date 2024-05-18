from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_user_settings, name='page_user_settings'),
]

