import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Client, Project, User
from .serializers import ClientDetailSerializer, ClientDetailSerializerget, ClientSerializer,  ProjectSerializer, ProjectSerializer29, ProjectSerializer9, UserSerializer
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





# @api_view(['POST'])
# def create_project9(request):
#     serializer = ProjectSerializer9(data=request.data)
#     if serializer.is_valid():
#         project = serializer.save()
#         return Response(ProjectSerializer(project).data, status=201)
#     return Response(serializer.errors, status=400)
#     # serializer = ProjectSerializer9(data=request.data)
  
#     # if serializer.is_valid():
#     #     project = serializer.save()
#     #     return Response(project, status=201)
#     # return Response(serializer.errors, status=400)


@api_view(['POST'])
def create_project9(request):
    # Retrieve the project data from the request payload
    project_data = request.data
    cid=project_data.get("client")
    client = get_object_or_404(Client, pk=cid)
    serializer = ProjectSerializer(data=project_data)
    if serializer.is_valid():
        project = serializer.save()

        # Serialize project details
        project_details = ProjectSerializer9(project).data
        return Response(project_details)
   # return Response(client)

   


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Project
from .serializers import ProjectSerializer

@api_view(['POST'])
def create_project(request):
    # Retrieve the project data from the request payload
    project_data = request.data

    # Extract the client ID from the project data
    client_id = project_data.get('client_id')

    # Retrieve the client instance based on the client_id
    client = get_object_or_404(Client, pk=client_id)

    # Serialize the project data
    serializer = ProjectSerializer(data=project_data)
    if serializer.is_valid():
        # Save the project instance
        project = serializer.save()

        # Retrieve the user IDs associated with the project
        user_ids = project_data.get('users', [])

        # Retrieve the user instances based on the provided user IDs
        users = User.objects.filter(id__in=user_ids)

        # Serialize the project details
        project_details = ProjectSerializer(project).data

        # Serialize the user details
        user_details = [{'id': user.id, 'username': user.username} for user in users]

        # Include user details in the project details
        project_details['users'] = user_details

        return Response(project_details, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def create_projectiii(request):
    serializer = ProjectSerializer29(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)