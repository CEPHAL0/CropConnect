from django.db import models
from provinces.models import Province


class District(models.Model):
    name = models.CharField(max_length=100)
    EcologicalRegions = models.TextChoices("EcologicalRegions", "hill mountain terai")
    province = models.ForeignKey(Province, on_delete=models.RESTRICT)
    ecological_region = models.CharField(blank=True, choices=EcologicalRegions)

    class Meta:
        db_table = "districts"
