from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(default=None)
    serial = models.TextField(default=None)
    date = models.DateTimeField(default=None)
    region = models.TextField(default=None)
    price = models.IntegerField(default=None)
    seller = models.TextField(default=None)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        Board.objects.filter(date__lte=timezone.now())\
                    .order_by('created_date')
        return self.title

from django.contrib import admin
from board.models import Board

admin.site.register(Board)