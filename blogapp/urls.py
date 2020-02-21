from django.urls import path
from .blogapp import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]