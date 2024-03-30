from django.db import models
from django.contrib.auth.models import User as AuthUser

class User(models.Model):
    user_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default='me')

    def __str__(self):
        return self.user_name

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default='Rohit')
  #  updated_at = models.DateTimeField(auto_now=True)  # Add updated_at field
    #users = models.ManyToManyField(AuthUser, related_name='clients', through='ClientMembership')

    def __str__(self):
        return self.client_name

# class ClientMembership(models.Model):
#     user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, default='Ganesh')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
   # client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    #client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user=models.ManyToManyField(User)
  
    def __str__(self):
        return self.project_name
