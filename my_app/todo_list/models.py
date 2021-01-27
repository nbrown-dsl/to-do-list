from django.db import models
from django.db.models.fields.related import ForeignKey
from django.forms.forms import Form 
import inspect


# CREATE DATABASE MIGRATION: python manage.py makemigrations
# MIGRATE THE DATABASE: python manage.py migrate #
# use in terminal from 'todo_list.models import List' to query list table #

# create model classes that correspond to database tables

#people who may have task responsibilities
class persons(models.Model):
    name =  models.CharField(max_length=200,default=None,null=True)
    email = models.CharField(max_length=400,default=None,null=True)
     
    # so that name appears in select field
    def __str__(self): 
         return self.name
    # to display in list table
    def summaryTitle(self):
        return self.name
    #hack to get name of object class passed from entity edit list to view def
    def className(self):
        return 'persons'

#fields that may be listed in protocol form    
class List(models.Model):
    forename =  models.CharField(max_length=50,default=None,null=True)
    surname = models.CharField(max_length=50,default=None,null=True)
    YEAR_LEVELS = (
    ('1', 'yr 1'),
    ('2', 'yr 2'),
    ('3', 'yr 3')
    )
    yearLevel = models.CharField(max_length=1, choices=YEAR_LEVELS,default=None,null=True)
    completed = models.BooleanField(default=False,null=True)
    arrivalDate = models.DateField(null=True)
    leavingDate = models.DateField(null=True)
    people = models.ManyToManyField(persons)

    def __str__(self):
        return self.item + ' completed: ' + str(self.completed)

    def fields(self):
        return (['forename','surname'])

class ListFields(models.Model):
    field = models.CharField(max_length=50, default="field")

    def __str__(self):
        return self.field
    




#protocol type set by fields selected and tasks allocated
class protocoltype(models.Model):
    protocolTypeName =  models.CharField(max_length=100,)
    description =  models.CharField(max_length=250,default='')
    protocolFields =  models.ManyToManyField(ListFields)

    

    # def __init__(self,protocolTypeName,description):       
    #     self.protocolTypeName = protocolTypeName 
    #     self.description = description
    #     self.form = List() #composition

    def summaryTitle(self):
        return self.protocolTypeName
    #hack to get name of object class passed from entity edit list to view def
    def className(self):
        return 'protocoltype'
    def __str__(self): 
         return self.protocolTypeName

#protocol object with field data, inherits List class fields    
class protocol(List,models.Model):
    type = models.ForeignKey(protocoltype,on_delete=models.CASCADE)
    # form = models.OneToOneField(List,on_delete=models.CASCADE)



class task(models.Model): 
    TaskDescription =  models.CharField(max_length=250,default='') 
    protocolType = models.ForeignKey(protocoltype,on_delete=models.DO_NOTHING)

    def summaryTitle(self):
        return self.TaskDescription
    #hack to get name of object class passed from entity edit list to view def
    def className(self):
        return 'task'
    
class taskdata(models.Model):
    completed = models.BooleanField(default=False)
    completionDate = models.DateField(null=True)
    notes =  models.CharField(max_length=250,default='')
    protocol = models.ForeignKey(protocol,on_delete=models.CASCADE)
    task = models.ForeignKey(task,on_delete=models.CASCADE)

# class responsibility(models.Model):
    # task = models.ForeignKey(task,on_delete=models.CASCADE)
    # person = models.ForeignKey(persons,on_delete=models.DO_NOTHING) 
