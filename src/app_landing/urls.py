from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_landing, name='page_landing'),
    path('about/', views.page_about, name='page_about'),
]

