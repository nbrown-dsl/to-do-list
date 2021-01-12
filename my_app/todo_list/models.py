from django.db import models
from django.db.models.fields.related import ForeignKey
from django.forms.forms import Form 

# CREATE DATABASE MIGRATION: python manage.py makemigrations
# MIGRATE THE DATABASE: python manage.py migrate #
# use in terminal from 'todo_list.models import List' to query list table #

# create database table with attributes.

class persons(models.Model):
    name =  models.CharField(max_length=200)
    email = models.CharField(max_length=400,default='')   
    # so that name appears in select field
    def __str__(self): 
         return self.name
    
class List(models.Model):
    forename =  models.CharField(max_length=50,default='')
    surname = models.CharField(max_length=50,default='')
    YEAR_LEVELS = (
    ('1', 'yr 1'),
    ('2', 'yr 2'),
    ('3', 'yr 3')
    )
    yearLevel = models.CharField(max_length=1, choices=YEAR_LEVELS,default='')
    completed = models.BooleanField(default=False)
    arrivalDate = models.DateField(null=True)
    leavingDate = models.DateField(null=True)
    people = models.ManyToManyField(persons)

    def __str__(self):
        return self.item + ' completed: ' + str(self.completed)


class protocol_type(models.Model):
    description =  models.CharField(max_length=250,default='') 
    name =  models.CharField(max_length=100,)

class protocol(models.Model):
    type = models.ForeignKey(protocol_type,on_delete=models.DO_NOTHING)
    form = models.OneToOneField(List,on_delete=models.CASCADE)

class protocol_field(models.Model):
    field = models.ForeignKey(List,on_delete=models.CASCADE)
    type = models.ForeignKey(protocol_type,on_delete=models.CASCADE)

class task(models.Model): 
    description =  models.CharField(max_length=250,default='') 
    protocolType = models.ForeignKey(protocol_type,on_delete=models.DO_NOTHING)
    
class task_Data(models.Model):
    completed = models.BooleanField(default=False)
    completionDate = models.DateField(null=True)
    notes =  models.CharField(max_length=250,default='')
    protocol = models.ForeignKey(protocol,on_delete=models.CASCADE)
    task = models.ForeignKey(task,on_delete=models.CASCADE)

class responsibility(models.Model):
    task = models.ForeignKey(task,on_delete=models.CASCADE)
    person = models.ForeignKey(persons,on_delete=models.CASCADE) 
