"""Django Models Utilities"""
# Django 
from django.db import models

class CRideModel(models.Model):
  created = models.DateTimeField(
    'created at',
    auto_now_add=True,
    help_text='Date time on which the objetct was created'
  )


  modified = models.DateTimeField(
    'created at',
    auto_now_add=True,
    help_text='Date time on which the objetct was last modified'
  )

  class Meta:
    abstract = True
    get_lastest_by = 'created'
    ordering = ['-created', '-modified']