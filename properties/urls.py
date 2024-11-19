from django.urls import path

from . import views

app_name = 'properties'

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('<int:property_id>/', views.property_detail, name='property_detail'),
    path('add/', views.add_property, name='add_property'),
    path('<int:property_id>/add-image/', views.add_property_image, name='add_property_image'),
    path('add-category/', views.add_category, name='add_category'),
]