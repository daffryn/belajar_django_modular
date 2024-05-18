from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_beranda, name='page_beranda'),
    path('status/', views.page_status, name='page_status'),
]

