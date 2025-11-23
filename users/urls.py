from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import logout_view


urlpatterns = [
    # /users/ -> signup page
    # path('', views.signup, name='signup'),
    path('register/', views.signup, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Use custom logout view so logout can be triggered via GET (e.g. from a link)
    path('logout/', views.logout_view, name='logout'),
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