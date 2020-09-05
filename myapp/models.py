from django.db import models

#Create your models here.craete django models for 
#how to create django models for the data inserting into the database fo the given table.
class Todoitem(models.Model):
    content=models.TextField()
class Node(models.Model):
    data=models.TextField()