from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # /users/ -> signup page
    # path('', views.signup, name='signup'),
    path('register/', views.signup, name='register'),
   path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]






# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#    path('register/', views.register, name='register'),
   
    
# ]  

# project/urls.py (Example)
# from django.contrib.auth import views as auth_views

# urlpatterns = [
#     # ... other paths
#     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     # ...
# ]