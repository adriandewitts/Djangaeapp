from django.db import models

class ServiceRule(models.Model):
    permission = models.CharField(max_length=30)
    read = models.CharField(max_length=30)
    table = models.CharField(max_length = 30)

    class Meta:
        db_table = 'ServiceRule'