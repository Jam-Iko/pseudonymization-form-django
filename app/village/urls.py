from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-view'),
    path('exercise/<slug:pk>', views.ExerciseView.as_view(), name='exercise-view'),
    path('exercise/<slug:pk>/launch', views.launch_exercise, name='exercise-launch-view'),
    path('exercise/<slug:pk>/stop', views.stop_portainer_exercise, name='exercise-stop-view'),
]