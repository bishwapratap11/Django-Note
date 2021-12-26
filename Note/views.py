from django.http import response
from django.shortcuts import render
import requests
import json

# Create your views here.

def index(request):
    response = requests.get('https://dammari-note.herokuapp.com/api/').json()
    print(response)
    return render(request, 'index.html', {'list': response})

def create(request):
    return render(request, 'New.html')

def view(request, id):
    response = requests.get('https://dammari-note.herokuapp.com/api/note/'+ id + '/').json()
    return render(request, 'update.html', {'id': id, 'response': response})
