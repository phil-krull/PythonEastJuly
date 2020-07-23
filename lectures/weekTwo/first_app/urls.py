from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('name/<str:name>', views.show_name),
    path('process', views.process_form),
    path('success', views.success),
    path('region', views.add_region),
    path('grape', views.add_grape),
    path('producer', views.add_producer),
    path('connect_region_to_producer', views.region_to_producer)
]

