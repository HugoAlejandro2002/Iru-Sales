from django.contrib.auth.models import User
from django.db import models

from team.models import Team

class Customer(models.Model):
    team = models.ForeignKey(Team, related_name='customers', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255, blank=True, null = True)
    created_by = models.ForeignKey(User,related_name='customers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

class Note(models.Model):
    team = models.ForeignKey(Team, related_name='notes', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, related_name='notes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)