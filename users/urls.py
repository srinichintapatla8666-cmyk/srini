from django.urls import path
from . import views

urlpatterns = [
    # /users/ -> signup page
    path('', views.signup, name='signup'),

    # Legacy/alternate URL: /users/register/
    path('register/', views.signup, name='register'),
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