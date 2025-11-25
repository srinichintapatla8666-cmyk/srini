from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('add/', views.ItemCreateView.as_view(), name='create_item'), 
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),

] 