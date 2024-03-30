import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Client, Project, User
from .serializers import ClientDetailSerializer, ClientDetailSerializerget, ClientSerializer,  ProjectSerializer, ProjectSerializer29, ProjectSerializer9, ProjectSerializer_for_post, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'GET':
      
        serializer = ClientDetailSerializerget(client)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = ClientDetailSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=204)



@api_view(['GET','POST'])
def project_list(request):
    if request.method=='GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        Response(serializer.errors, status=400)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'GET':
        serializer =ProjectSerializer(project,many=True)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=204)    


@api_view(['POST'])
def create_project(request):
    serializer = ProjectSerializer_for_post(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)