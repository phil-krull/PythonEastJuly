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

    # routes for semi-restful(only get and post request) routing (restful routing get, post, patch/put, delete)
    # 7 main urls for each database entry
    
    # get all
    # path('regions', views.index)

    # # get one
    # path('regions/<int:region_id', views.show)

    # # add one (get, form)
    # path('regions/new', views.new)

    # # create one (post)
    # path('regions/create', views.create)

    # # edit one (get, form)
    # path('regions/<int:region_id/edit', views.edit)

    # # update one (post)
    # path('regions/<int:region_id>/update', views.update)

    # # delete one (get)
    # path('regions/<int:region_id>/delete', views.delete)
]

