
import os
import uuid
from django.db import models


# Create your models here.

STATUS = (
    ('new', 'New'),
    ('read', 'Read'),
    ('closed', 'Closed'),
)


class Contact(models.Model):
    subject = models.CharField(max_length=25, null=True)
    status = models.CharField(max_length=6, choices=STATUS, default='new')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'