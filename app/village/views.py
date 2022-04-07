from email import message
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.utils.safestring import mark_safe
from .models import Village, Exercise
import os
import requests


def index(request):
    context = {}
    pk = os.getenv(f'VILLAGE')
    context['village'] = Village.objects.get(pk=pk)
    context['exercises'] = Exercise.objects.filter(village=pk)
    return render(request, 'village/village.html', context)


class ExerciseView(DetailView):
    model = Exercise
    context_object_name = 'exercise'
    template_name = 'village/exercise.html'


def connect_portainer(portainer_server, ip):
    username = os.getenv(f'PORTAINER_USERNAME')
    password = os.getenv(f'PORTAINER_PASSWORD')
    req = requests.post(f'https://{ip}:9443/api/auth', 
                    json={'username': username, 'password': password},
                    verify=False)
    if req.status_code == 200:
        jwt = req.json()
        return jwt['jwt']
    else:
        return None


def launch_exercise(request, pk):
    context = {}
    exercise = Exercise.objects.filter(pk=pk).values()[0]
    context['exercise'] = exercise
    if request.method == 'POST':
        portainer_server = exercise["portainer_server"]
        stack_id =  exercise["portainer_stack_id"]
        ip =  exercise["portainer_ip"]
        link = exercise["portainer_link"]
        title = exercise["title"]
        jwt = connect_portainer(portainer_server, ip)
        if not jwt:
            messages.error(request, "Failed to connect")
            return redirect('exercise-view', pk)
        req = requests.post(f'https://{ip}:9443/api/stacks/{stack_id}/start', 
                        headers={"Authorization": f"Bearer {jwt}"},
                        verify=False)
        print(req)
        # 409 stack already started
        if req.status_code == 200 or req.status_code == 409:
            messages.success(request, mark_safe(f"Please follow link to view <a href='http://{ip}{link}' target='_blank' rel='noopener noreferrer'>{title}</a>"))
        return redirect('exercise-view', pk)
    return redirect('exercise-view', pk)