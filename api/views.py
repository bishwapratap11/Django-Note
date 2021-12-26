from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import NotesSerializer
from .models import Notes
import json
# Create your views here.

@api_view(['POST'])
def create(request):
    print(request.data)
    serializerss = NotesSerializer(data=request.data)
    
    

    if serializerss.is_valid():
        serializerss.save()
        print('done')
        return Response(serializerss.data)
    else:
        print('none')
        return Response(serializerss.data)

@api_view(['GET'])
def notes(request):
    notes = Notes.objects.all().order_by('-id')
    serializer = NotesSerializer(notes, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def note(request, id):
    notes = Notes.objects.get(id=id)
    serializer = NotesSerializer(notes)
    return Response(serializer.data)

@api_view(['PUT'])
def update(request, id):
    notes = Notes.objects.get(id=id)
    serializerss = NotesSerializer(instance=notes, data=request.data)
    if serializerss.is_valid():
        serializerss.save()
        print('done')
        return Response(serializerss.data)
    else:
        print('none')
        return Response(serializerss.data)

@api_view(['DELETE'])
def remove(request, id):
    notes = Notes.objects.get(id=id)
    notes.delete()

    return Response('Deleted Successfully')