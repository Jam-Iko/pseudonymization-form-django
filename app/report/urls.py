from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-view'),
    path('create/', views.reportcreateview, name='create-report-view')
]