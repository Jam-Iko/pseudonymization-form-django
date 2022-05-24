from email import message
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.utils.safestring import mark_safe
from cryptography.fernet import Fernet
from .models import Village, Exercise
import os
import requests
import json

_KEY = bytes(os.getenv('KEY', None), "utf-8")
f = Fernet(_KEY)

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


def launch_exercise(request, pk):
    context = {}
    exercise = Exercise.objects.filter(pk=pk).values()[0]
    context['exercise'] = exercise
    
    _FLASK_API = os.getenv('FLASK_API')
    _FLASK_API_KEY = os.getenv('FLASK_API_KEY')
    x_api_key = f.encrypt(bytes(pk, "utf-8"))
    if request.method == 'POST':
        req = requests.post(f'{_FLASK_API}:5000/launch_exercise', 
                        json={"exercise": pk},
                        headers={"X-Api-Key": x_api_key},
                    )
        if not req.status_code == 200:
            messages.error(request, "Failed to connect")
            return redirect('exercise-view', pk)
        res = json.loads(req.content)
        messages.success(request, mark_safe(f"Setup is complete. Please follow steps to complete exercise</a>"))
        return redirect('exercise-view', pk)
    return redirect('exercise-view', pk)


# PORTAINER SETUP
def connect_portainer(ip):
    pk = os.getenv(f'VILLAGE')
    village = Village.objects.get(pk=pk)
    username = os.getenv(f'PORTAINER_USERNAME')
    password = os.getenv(f'PORTAINER_PASSWORD')
    req = requests.post(f'https://{ip}:9443/api/auth', 
                    json={'username': username, 'password': password},
                    verify=False)
    if req.status_code == 200:
        jwt = req.json()
        print(jwt)
        village.portainer_jwt = jwt['jwt']
        village.save()
        return jwt['jwt']
    else:
        return None


def stop_portainer_exercise(request, pk):
    context = {}
    exercise = Exercise.objects.filter(pk=pk).values()[0]
    context['exercise'] = exercise
    pk_village = os.getenv(f'VILLAGE')
    village = Village.objects.filter(pk=pk_village).values()[0]
    if request.method == 'POST':
        stack_id =  exercise["portainer_stack_id"]
        ip =  exercise["portainer_ip"]
        jwt = village['portainer_jwt']
        if not jwt:
            try:
                jwt = connect_portainer(ip)
            except Exception as e:
                print(e)
                messages.error(request, "Failed to connect")
                return redirect('exercise-view', pk)
        req = requests.post(f'https://{ip}:9443/api/stacks/{stack_id}/stop', 
                        headers={"Authorization": f"Bearer {jwt}"},
                        verify=False)
        print(req.status_code)
        if req.status_code == 200 or req.status_code == 400:
            messages.success(request, mark_safe(f"Exercise is stopped"))
            return redirect('exercise-view', pk)
    return redirect('exercise-view', pk)


def launch_portainer_exercise(request, pk):
    context = {}
    exercise = Exercise.objects.filter(pk=pk).values()[0]
    context['exercise'] = exercise
    pk_village = os.getenv(f'VILLAGE')
    village = Village.objects.filter(pk=pk_village).values()[0]
    if request.method == 'POST':
        stack_id =  exercise["portainer_stack_id"]
        ip =  exercise["portainer_ip"]
        link = exercise["portainer_link"]
        title = exercise["title"]
        jwt = json.dumps(village['portainer_jwt'])
        print(jwt)
        if not jwt:
            print("Need to get jwt")
            jwt = connect_portainer(ip)
            if not jwt:
                messages.error(request, "Failed to connect")
                return redirect('exercise-view', pk)
        req = requests.post(f'https://{ip}:9443/api/stacks/{stack_id}/start', 
                        headers={"Authorization": f"Bearer {jwt}"},
                        verify=False)
        if req.status_code == 401:
            jwt = connect_portainer(ip)
            if not jwt:
                messages.error(request, "Failed to connect")
                return redirect('exercise-view', pk)
            req = requests.post(f'https://{ip}:9443/api/stacks/{stack_id}/start', 
                    headers={"Authorization": f"Bearer {jwt}"},
                    verify=False)
            if req.status_code == 200 or req.status_code == 409:
                messages.success(request, mark_safe(f"Please follow link to view <a href='http://{ip}{link}' target='_blank' rel='noopener noreferrer'>{title}</a>"))
                return redirect('exercise-view', pk)
        if req.status_code == 200 or req.status_code == 409:
            messages.success(request, mark_safe(f"Please follow link to view <a href='http://{ip}{link}' target='_blank' rel='noopener noreferrer'>{title}</a>"))
            return redirect('exercise-view', pk)
    return redirect('exercise-view', pk)