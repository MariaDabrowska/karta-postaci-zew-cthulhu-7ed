from django.db import models
from random import randint


class Kostka(models.Model):
    ilosc_scian = models.PositiveSmallIntegerField(primary_key=True)

    def rzut(self):
        return randint(1, self.ilosc_scian)

    def rzuty_modyfikowane1(self):
        return (self.rzut() + self.rzut() + self.rzut()) * 5

    def rzuty_modyfikowane2(self):
        return (self.rzut() + self.rzut() + 6) * 5
