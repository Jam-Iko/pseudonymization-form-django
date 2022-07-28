from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_pseudo, name='select-pseudo-view')
]