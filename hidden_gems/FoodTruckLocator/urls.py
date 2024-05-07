from django.urls import path
from . import views

urlpatterns = [
    path('', views.query_csv, name='show_map')
]
