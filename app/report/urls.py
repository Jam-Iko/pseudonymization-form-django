from django.urls import path
from . import views

urlpatterns = [
    path('', views.reportcreateview, name='create-report-view')
]