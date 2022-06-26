from abc import ABC, abstractmethod

from django.db import models


class Przelicznik(models.Model, ABC):
    @abstractmethod
    def pokaz_wartosci(self, value):
        return value, value // 2, value // 5


class ZestawCechPostaci(models.Model):
    sila = models.PositiveSmallIntegerField()
    kondycja = models.PositiveSmallIntegerField()
    budowa_ciala = models.PositiveSmallIntegerField()
    zrecznosc = models.PositiveSmallIntegerField()
    wyglad = models.PositiveSmallIntegerField()
    integligencja = models.PositiveSmallIntegerField()
    moc = models.PositiveSmallIntegerField()
    wyksztalcenie = models.PositiveSmallIntegerField()
    szczescie = models.PositiveSmallIntegerField()
    mod_obr = models.CharField(max_length=4)
    krzepa = models.SmallIntegerField()
    wytrzymalosc = models.PositiveSmallIntegerField()
    ruch = models.PositiveSmallIntegerField()


class Umiejetnosc(models.Model):
    aktorstwo = models.PositiveSmallIntegerField(default=5)
    antropologia = models.PositiveSmallIntegerField(default=1)
    archeologia = models.PositiveSmallIntegerField(default=1)
    astronomia = models.PositiveSmallIntegerField(default=1)
    bicz = models.PositiveSmallIntegerField(default=5)
    bijatyka = models.PositiveSmallIntegerField(default=25)
    biologia = models.PositiveSmallIntegerField(default=1)
    botanika = models.PositiveSmallIntegerField(default=1)
    bron_artyleryjska = models.PositiveSmallIntegerField(default=1)
    bron_ciezka = models.PositiveSmallIntegerField(default=10)
    bron_krotka = models.PositiveSmallIntegerField(default=20)
    bron_obuchowa = models.PositiveSmallIntegerField(default=10)
    charakteryzacja = models.PositiveSmallIntegerField(default=5)
    chemia = models.PositiveSmallIntegerField(default=1)
    czytanie_z_ruchu_warg = models.PositiveSmallIntegerField(default=1)
    elektronika = models.PositiveSmallIntegerField(default=1)
    elektryka = models.PositiveSmallIntegerField(default=10)
    falszerstwo = models.PositiveSmallIntegerField(default=1)
    farmacja = models.PositiveSmallIntegerField(default=1)
    fizyka = models.PositiveSmallIntegerField(default=1)
    fotografia = models.PositiveSmallIntegerField(default=5)
    gadanina = models.PositiveSmallIntegerField(default=5)
    garota = models.PositiveSmallIntegerField(default=15)
    geologia = models.PositiveSmallIntegerField(default=1)
    hipnoza = models.PositiveSmallIntegerField(default=1)
    historia = models.PositiveSmallIntegerField(default=5)
    inzynieria = models.PositiveSmallIntegerField(default=1)
    jezdziectwo = models.PositiveSmallIntegerField(default=5)
    jezyk_obcy = models.PositiveSmallIntegerField(default=1)
    jezyk_ojczysty = models.PositiveSmallIntegerField(default=0)                    # !!!!!!!!!!
    karabin = models.PositiveSmallIntegerField(default=25)
    karabin_maszynowy = models.PositiveSmallIntegerField(default=10)
    korzystanie_z_bibliotek = models.PositiveSmallIntegerField(default=20)
    korzystanie_z_komputerow = models.PositiveSmallIntegerField(default=5)
    kryminalistyka = models.PositiveSmallIntegerField(default=5)
    kryptografia = models.PositiveSmallIntegerField(default=1)
    ksiegowosc = models.PositiveSmallIntegerField(default=5)
    luk = models.PositiveSmallIntegerField(default=15)
    majetnosc = models.PositiveSmallIntegerField(default=0)
    mtematyka = models.PositiveSmallIntegerField(default=10)
    materialy_wybuchowe = models.PositiveSmallIntegerField(default=1)
    mechanika = models.PositiveSmallIntegerField(default=10)
    medycyna = models.PositiveSmallIntegerField(default=1)
    meteorologia = models.PositiveSmallIntegerField(default=1)
    miecz = models.PositiveSmallIntegerField(default=20)
    miotacz_ognia = models.PositiveSmallIntegerField(default=10)
    mity_cthulhu = models.PositiveSmallIntegerField(default=0)
    nasluchiwanie = models.PositiveSmallIntegerField(default=20)
    nauka = models.PositiveSmallIntegerField(default=1)
    nawigacja = models.PositiveSmallIntegerField(default=10)
    nurkowanie = models.PositiveSmallIntegerField(default=1)
    obsluga_ciezkiego_sprzetu = models.PositiveSmallIntegerField(default=1)
    okultyzm = models.PositiveSmallIntegerField(default=5)
    perswazja = models.PositiveSmallIntegerField(default=10)
    pierwsza_pomoc = models.PositiveSmallIntegerField(default=30)
    pilotowanie = models.PositiveSmallIntegerField(default=1)
    pila_lancuchowa = models.PositiveSmallIntegerField(default=10)
    pistolet_maszynowy = models.PositiveSmallIntegerField(default=15)
    plywanie = models.PositiveSmallIntegerField(default=20)
    prawo = models.PositiveSmallIntegerField(default=5)
    prowadzenie_samochodu = models.PositiveSmallIntegerField(default=20)
    psychoanaliza = models.PositiveSmallIntegerField(default=1)
    psychologia = models.PositiveSmallIntegerField(default=10)
    rzucanie = models.PositiveSmallIntegerField(default=20)
    skakanie = models.PositiveSmallIntegerField(default=20)
    spostrzegawczosc = models.PositiveSmallIntegerField(default=25)
    strzelba = models.PositiveSmallIntegerField(default=25)
    sztuka_przetrwania = models.PositiveSmallIntegerField(default=10)
    sztuka_rzemioslo = models.PositiveSmallIntegerField(default=5)
    sztuki_piekne = models.PositiveSmallIntegerField(default=5)
    slusarstwo = models.PositiveSmallIntegerField(default=1)
    topor_siekiera = models.PositiveSmallIntegerField(default=15)
    tresura_zwierzat = models.PositiveSmallIntegerField(default=5)
    tropienie = models.PositiveSmallIntegerField(default=10)
    ukrywanie = models.PositiveSmallIntegerField(default=20)
    unik = models.PositiveSmallIntegerField(default=0)                              # !!!!!!!!!!!!!!
    urok_osobisty = models.PositiveSmallIntegerField(default=15)
    wiedza_o_naturze = models.PositiveSmallIntegerField(default=10)
    wiedza_tajemna = models.PositiveSmallIntegerField(default=1)
    wlocznia = models.PositiveSmallIntegerField(default=20)
    wspinaczka = models.PositiveSmallIntegerField(default=20)
    wycena = models.PositiveSmallIntegerField(default=5)
    zastraszanie = models.PositiveSmallIntegerField(default=15)
    zoologia = models.PositiveSmallIntegerField(default=1)
    zreczne_palce = models.PositiveSmallIntegerField(default=10)


class Profesja(models.Model):

    nazwa = models.CharField(max_length=50, primary_key=True)
    majetnosc_min = models.PositiveSmallIntegerField()
    majetnosc_max = models.PositiveSmallIntegerField()
    um_stale = models.CharField(max_length=200)
    wybor1 = models.CharField(max_length=200, null=True)
    wybor2 = models.CharField(max_length=200, null=True)
    wybor3 = models.CharField(max_length=200, null=True)


class Postac(models.Model):
    pass
