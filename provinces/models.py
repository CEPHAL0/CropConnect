from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'provinces'
