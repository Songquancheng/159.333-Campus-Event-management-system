from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register),
    path('api/login/', views.login_view),

    path('', views.index, name='vue_home'),
]
