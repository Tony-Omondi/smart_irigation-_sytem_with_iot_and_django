from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index/Homepage URL
    path('login/', views.login_view, name='login'),  # Added trailing slash
    path('signup/', views.signup_view, name='signup'),  # Added trailing slash
    path('logout/', views.logout_view, name='logout'),  # Added trailing slash
    
]
