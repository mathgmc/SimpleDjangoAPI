from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.get_data, name='get_items'),
    path('items/', views.post_data, name='create_item'),
    path('items/<int:pk>/', views.get_data_by_id, name='get_item_by_id'),
    path('items/<int:pk>/', views.update_data, name='update_item'),
    path('items/<int:pk>/', views.delete_data, name='delete_item'),
]