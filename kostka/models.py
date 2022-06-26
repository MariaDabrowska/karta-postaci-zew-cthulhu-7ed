from django.db import models
from random import randint


class Kostka(models.Model):
    ilosc_scian = models.PositiveSmallIntegerField(primary_key=True)

    def rzut(self):
        return randint(1, self.ilosc_scian)
