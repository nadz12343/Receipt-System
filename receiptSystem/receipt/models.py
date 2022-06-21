from enum import auto
from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse

# Create your models here.

class Receipt(models.Model):
    name = models.CharField(max_length=20)
    cost = models.FloatField(default=0)
    location = models.CharField(max_length = 6)
    creation_date = models.DateField()

    def get_name(self):
        return self.name

    def get_receipt(self):
        return {"id": self.id, 
                "name": self.name, 
                "cost": self.cost, 
                "location": self.location, 
                "creation_date":self.creation_date,
                "update_api": reverse('update_receipt', kwargs= {"id": self.id}),
                "delete_api": reverse('delete_receipt', kwargs={"id": self.id})}
        
    
    def get_receipt_arr(self):
        return [self.id, self.name, self.cost, self.location, self.creation_date]


    def get_cost(self):
        return self.cost
    
    def get_id(self):
        return self.id

    def __str__(self):
        return f"{self.name} the cost is: {self.cost} and the date this receipt was created is: {self.creation_date}"