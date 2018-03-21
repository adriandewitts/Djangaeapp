# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from djangae.fields import ListField

class MinimalPair(models.Model):
    word_a = models.CharField(max_length = 32)
    word_b = models.CharField(max_length = 32)
    exclude = models.BooleanField(default = False)
    confirmed = models.BooleanField(default = True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    client_id = models.CharField(max_length = 40, default = 'admin')

    class Meta:
        db_table = 'MinimalPair'


class WordSetLevel(models.Model):
    level = models.IntegerField()
    words = ListField(models.CharField(max_length=32))

    class Meta:
        db_table = 'WordSetLevel'