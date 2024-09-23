from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index/Homepage URL
    # path('login/', views.login_view, name='login'),
    # path('signup/', views.signup_view, name='signup'),
]
