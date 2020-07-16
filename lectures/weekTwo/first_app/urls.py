from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('name/<str:name>', views.show_name),
    path('process', views.process_form),
    path('success', views.success)
]

