from django.db import models


class Kostka(models.Model):
    ilosc_scian = models.PositiveSmallIntegerField(primary_key=True)
