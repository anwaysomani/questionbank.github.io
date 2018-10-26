"""
Model for question, link to db
app: latex

Developer: Anway Somani

"""

from django.db import models
from ..constant import MOD_CHOICES, MARKS_CHOICES, PRI_CHOICES
from .fields import Subject

# Model: Question
class Question(models.Model):
    block = models.IntegerField(blank=True, help_text='Enter above block value as block id here')
    modules = models.CharField(max_length=100, choices=MOD_CHOICES)
    question = models.CharField(max_length=300, unique=True)
    marks = models.IntegerField(choices=MARKS_CHOICES, null=True)
    priority = models.IntegerField(choices=PRI_CHOICES)
    notes = models.CharField(max_length=300)

    def __str__(self):
        return self.question
