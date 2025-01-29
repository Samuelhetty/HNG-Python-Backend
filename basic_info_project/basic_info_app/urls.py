from django.urls import path
from . import views


urlpatterns = [
    path('api/basic_info_app/', views.get_info, name='get_info'),
]