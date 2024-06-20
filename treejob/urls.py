from django.urls import path

from . import views

urlpatterns = [
    path('treejob/', views.trees, name='treejob'),
]