from abc import ABC, abstractmethod

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# class Przelicznik(models.Model, ABC):
#     @abstractmethod
#     def pokaz_wartosci(self, value):
#         return value, value // 2, value // 5


class ZestawCechPostaci(models.Model):
    sila = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    kondycja = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    budowa_ciala = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    zrecznosc = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    wyglad = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    integligencja = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    moc = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    wyksztalcenie = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    szczescie = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    poczytalnosc = models.PositiveSmallIntegerField(validators=[MaxValueValidator(99)])
    punkty_magii = models.PositiveSmallIntegerField()
    mod_obr = models.CharField(max_length=4)
    krzepa = models.SmallIntegerField(validators=[MinValueValidator(-2), MaxValueValidator(2)])
    wytrzymalosc = models.PositiveSmallIntegerField(validators=[MaxValueValidator(18)])
    ruch = models.PositiveSmallIntegerField(validators=[MinValueValidator(2), MaxValueValidator(9)])


class Umiejetnosc(models.Model):
    aktorstwo = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(99)])
    antropologia = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    archeologia = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    astronomia = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    bicz = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(99)])
    bijatyka = models.PositiveSmallIntegerField(default=25, validators=[MinValueValidator(25), MaxValueValidator(99)])
    biologia = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    botanika = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    bron_artyleryjska = models.PositiveSmallIntegerField(default=1,
                                                         validators=[MinValueValidator(1), MaxValueValidator(99)])
    bron_ciezka = models.PositiveSmallIntegerField(default=10,
                                                   validators=[MinValueValidator(10), MaxValueValidator(99)])
    bron_krotka = models.PositiveSmallIntegerField(default=20,
                                                   validators=[MinValueValidator(20), MaxValueValidator(90)])
    bron_obuchowa = models.PositiveSmallIntegerField(default=10,
                                                     validators=[MinValueValidator(10), MaxValueValidator(90)])
    charakteryzacja = models.PositiveSmallIntegerField(default=5,
                                                       validators=[MinValueValidator(5), MaxValueValidator(99)])
    chemia = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    czytanie_z_ruchu_warg = models.PositiveSmallIntegerField(default=1,
                                                             validators=[MinValueValidator(1), MaxValueValidator(99)])
    elektronika = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    elektryka = models.PositiveSmallIntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(99)])
    falszerstwo = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    farmacja = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    fizyka = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    fotografia = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(99)])
    gadanina = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(99)])
    garota = models.PositiveSmallIntegerField(default=15, validators=[MinValueValidator(15), MaxValueValidator(99)])
    geologia = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    hipnoza = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    historia = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(99)])
    inzynieria = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    jezdziectwo = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(99)])
    jezyk_obcy = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    jezyk_ojczysty = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(99)])  # ważne przy tworzeniu!
    karabin = models.PositiveSmallIntegerField(default=25, validators=[MinValueValidator(25), MaxValueValidator(99)])
    karabin_maszynowy = models.PositiveSmallIntegerField(default=10,
                                                         validators=[MinValueValidator(10), MaxValueValidator(99)])
    korzystanie_z_bibliotek = models.PositiveSmallIntegerField(default=20,
                                                               validators=[MinValueValidator(20),
                                                                           MaxValueValidator(99)])
    korzystanie_z_komputerow = models.PositiveSmallIntegerField(default=5,
                                                                validators=[MinValueValidator(5),
                                                                            MaxValueValidator(99)])
    kryminalistyka = models.PositiveSmallIntegerField(default=5,
                                                      validators=[MinValueValidator(5), MaxValueValidator(99)])
    kryptografia = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    ksiegowosc = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(90)])
    luk = models.PositiveSmallIntegerField(default=15, validators=[MinValueValidator(15), MaxValueValidator(99)])
    majetnosc = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(99)])
    mtematyka = models.PositiveSmallIntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(99)])
    materialy_wybuchowe = models.PositiveSmallIntegerField(default=1,
                                                           validators=[MinValueValidator(1), MaxValueValidator(99)])
    mechanika = models.PositiveSmallIntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(99)])
    medycyna = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    meteorologia = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    miecz = models.PositiveSmallIntegerField(default=20, validators=[MinValueValidator(20), MaxValueValidator(99)])
    miotacz_ognia = models.PositiveSmallIntegerField(default=10,
                                                     validators=[MinValueValidator(10), MaxValueValidator(99)])
    mity_cthulhu = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(99)])
    nasluchiwanie = models.PositiveSmallIntegerField(default=20,
                                                     validators=[MinValueValidator(20), MaxValueValidator(99)])
    nauka = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    nawigacja = models.PositiveSmallIntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(99)])
    nurkowanie = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    obsluga_ciezkiego_sprzetu = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1),
                                                                                        MaxValueValidator(99)])
    okultyzm = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(99)])
    perswazja = models.PositiveSmallIntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(99)])
    pierwsza_pomoc = models.PositiveSmallIntegerField(default=30,
                                                      validators=[MinValueValidator(30), MaxValueValidator(99)])
    pilotowanie = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    pila_lancuchowa = models.PositiveSmallIntegerField(default=10,
                                                       validators=[MinValueValidator(10), MaxValueValidator(99)])
    pistolet_maszynowy = models.PositiveSmallIntegerField(default=15,
                                                          validators=[MinValueValidator(15), MaxValueValidator(99)])
    plywanie = models.PositiveSmallIntegerField(default=20, validators=[MinValueValidator(20), MaxValueValidator(99)])
    prawo = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(99)])
    prowadzenie_samochodu = models.PositiveSmallIntegerField(default=20,
                                                             validators=[MinValueValidator(20), MaxValueValidator(99)])
    psychoanaliza = models.PositiveSmallIntegerField(default=1,
                                                     validators=[MinValueValidator(1), MaxValueValidator(99)])
    psychologia = models.PositiveSmallIntegerField(default=10,
                                                   validators=[MinValueValidator(10), MaxValueValidator(99)])
    rzucanie = models.PositiveSmallIntegerField(default=20, validators=[MinValueValidator(20), MaxValueValidator(99)])
    skakanie = models.PositiveSmallIntegerField(default=20, validators=[MinValueValidator(20), MaxValueValidator(99)])
    spostrzegawczosc = models.PositiveSmallIntegerField(default=25,
                                                        validators=[MinValueValidator(25), MaxValueValidator(99)])
    strzelba = models.PositiveSmallIntegerField(default=25, validators=[MinValueValidator(25), MaxValueValidator(99)])
    sztuka_przetrwania = models.PositiveSmallIntegerField(default=10,
                                                          validators=[MinValueValidator(10), MaxValueValidator(99)])
    sztuka_rzemioslo = models.PositiveSmallIntegerField(default=5,
                                                        validators=[MinValueValidator(5), MaxValueValidator(99)])
    sztuki_piekne = models.PositiveSmallIntegerField(default=5,
                                                     validators=[MinValueValidator(5), MaxValueValidator(99)])
    slusarstwo = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    topor_siekiera = models.PositiveSmallIntegerField(default=15,
                                                      validators=[MinValueValidator(15), MaxValueValidator(99)])
    tresura_zwierzat = models.PositiveSmallIntegerField(default=5,
                                                        validators=[MinValueValidator(5), MaxValueValidator(99)])
    tropienie = models.PositiveSmallIntegerField(default=10, validators=[MinValueValidator(10), MaxValueValidator(99)])
    ukrywanie = models.PositiveSmallIntegerField(default=20, validators=[MinValueValidator(20), MaxValueValidator(99)])
    unik = models.PositiveSmallIntegerField(default=0,
                                            validators=[MaxValueValidator(99)])  # ważne przy tworzeniu postaci
    urok_osobisty = models.PositiveSmallIntegerField(default=15,
                                                     validators=[MinValueValidator(15), MaxValueValidator(99)])
    wiedza_o_naturze = models.PositiveSmallIntegerField(default=10,
                                                        validators=[MinValueValidator(10), MaxValueValidator(99)])
    wiedza_tajemna = models.PositiveSmallIntegerField(default=1,
                                                      validators=[MinValueValidator(1), MaxValueValidator(99)])
    wlocznia = models.PositiveSmallIntegerField(default=20, validators=[MinValueValidator(20), MaxValueValidator(99)])
    wspinaczka = models.PositiveSmallIntegerField(default=20, validators=[MinValueValidator(20), MaxValueValidator(99)])
    wycena = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5), MaxValueValidator(99)])
    zastraszanie = models.PositiveSmallIntegerField(default=15,
                                                    validators=[MinValueValidator(15), MaxValueValidator(99)])
    zoologia = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(99)])
    zreczne_palce = models.PositiveSmallIntegerField(default=10,
                                                     validators=[MinValueValidator(10), MaxValueValidator(99)])


class Profesja(models.Model):
    nazwa = models.CharField(max_length=50, primary_key=True)
    punkty_do_wydania = models.CharField(max_length=150)
    majetnosc_min = models.PositiveSmallIntegerField()
    majetnosc_max = models.PositiveSmallIntegerField()
    um_stale = models.CharField(max_length=200)
    wybor1 = models.CharField(max_length=200, null=True)
    wybor2 = models.CharField(max_length=200, null=True)
    wybor3 = models.CharField(max_length=200, null=True)
    wybor4 = models.CharField(max_length=200, null=True)


class Postac(models.Model):
    nazwa = models.CharField(max_length=218, null=False)
    uzytkownik = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='postac', blank=True, null=True
    )
    wiek = models.PositiveSmallIntegerField(validators=[MinValueValidator(15), MaxValueValidator(90)])
    cechy = models.ForeignKey(
        ZestawCechPostaci, on_delete=models.CASCADE, related_name='postac', blank=True, null=True
    )
    um = models.ForeignKey(
        Umiejetnosc, on_delete=models.CASCADE, related_name='postac', blank=True, null=True
    )
    profesja = models.ForeignKey(
        Profesja, on_delete=models.CASCADE, related_name='postac', blank=True, null=True
    )
    ekwipunek = models.CharField(max_length=1024, blank=True, null=True)
    historia = models.CharField(max_length=1024, blank=True, null=True)
    uzbrojenie = models.CharField(max_length=1024, blank=True, null=True)
