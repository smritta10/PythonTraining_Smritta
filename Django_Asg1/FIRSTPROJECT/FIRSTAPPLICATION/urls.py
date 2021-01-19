
from django.urls import path
from .import views

urlpatterns = [
    path('h/', views.func1, name='Hello'),
    path('t/', views.template_func, name='templatefunction'),
]
