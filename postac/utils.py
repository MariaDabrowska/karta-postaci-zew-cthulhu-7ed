from random import randint

from kostka.models import Kostka
from postac.models import ZestawCechPostaci


class GeneratorCech:
    @classmethod
    def wygeneruj_cechy(cls):
        k6 = Kostka.objects.get(ilosc_scian=6)

        sila = k6.rzuty_modyfikowane1()
        kondycja = k6.rzuty_modyfikowane1()
        budowa_ciala = k6.rzuty_modyfikowane2()
        zrecznosc = k6.rzuty_modyfikowane1()
        wyglad = k6.rzuty_modyfikowane1()
        inteligencja = k6.rzuty_modyfikowane2()
        moc = k6.rzuty_modyfikowane1()
        wyksztalcenie = k6.rzuty_modyfikowane2()
        szczescie = k6.rzuty_modyfikowane1()
        poczytalnosc = moc
        krzepa = cls._generuj_krzepa(sila=sila, budowa_ciala=budowa_ciala)
        punkty_magii = moc // 5
        mod_obr = cls._generuj_mod_ob(krzepa=krzepa)
        wytrzymalosc = cls._generuj_wytrzymalosc(kondycja=kondycja, budowa_ciala=budowa_ciala)
        ruch = cls._generuj_ruch(sila=sila, budowa_ciala=budowa_ciala, zrecznosc=zrecznosc)

        return ZestawCechPostaci.objects.create(
            sila=sila,
            kondycja=kondycja,
            budowa_ciala=budowa_ciala,
            zrecznosc=zrecznosc,
            wyglad=wyglad,
            integligencja=inteligencja,
            moc=moc,
            wyksztalcenie=wyksztalcenie,
            szczescie=szczescie,
            poczytalnosc=poczytalnosc,
            krzepa=krzepa,
            punkty_magii=punkty_magii,
            mod_obr=mod_obr,
            wytrzymalosc=wytrzymalosc,
            ruch=ruch
        )

    @staticmethod
    def _generuj_krzepa(sila, budowa_ciala):
        if sila + budowa_ciala < 65:
            return -2
        if sila + budowa_ciala < 85:
            return -1
        if sila + budowa_ciala < 125:
            return 0
        if sila + budowa_ciala < 165:
            return 1
        if sila + budowa_ciala < 205:
            return 2

    @staticmethod
    def _generuj_mod_ob(krzepa):
        if krzepa == 1:
            return '+1k4'  # krzepa + 1 rzut kostka k4? stała czy dynamiczna?
        if krzepa == 2:
            return '+1k6'
        return krzepa

    @staticmethod
    def _generuj_wytrzymalosc(kondycja, budowa_ciala):
        return (kondycja + budowa_ciala) // 10

    @staticmethod
    def _generuj_ruch(sila, budowa_ciala, zrecznosc):
        if sila > budowa_ciala and zrecznosc > budowa_ciala:
            return 9
        if sila < budowa_ciala and zrecznosc < budowa_ciala:
            return 7
        return 8


class ZastosujWiek:
    @staticmethod
    def test_rozwoju(value):
        k100 = Kostka.objects.get(ilosc_scian=100)
        k10 = Kostka.objects.get(ilosc_scian=10)
        if k100.rzut() > value:
            return k10.rzut()
        return 0

    @staticmethod
    def modyf_cech(pdo, *args):
        result = []
        i = 1
        for arg in args:
            if i != len(args):
                if pdo > arg:
                    mod = randint(0, arg)
                else:
                    mod = randint(0, pdo)
                arg -= mod
                pdo -= mod
                i += 1
            else:
                arg -= pdo
            result.append(arg)

        return result

    @classmethod
    def zastosuj_wiek(cls, cechy, wiek):
        if wiek < 20:
            k6 = Kostka.objects.get(6)
            cechy.wyksztalcenie -= 5
            cechy.szczescie = max(cechy.szczescie, k6.rzuty_modyfikowane1())
            punkty_do_odjecia = 5
            cechy.sila, cechy.budowa_ciala = cls.modyf_cech(punkty_do_odjecia, cechy.sila, cechy.budowa_ciala)

        elif wiek < 40:
            cechy.wyksztalcenie += cls.test_rozwoju(cechy.wyksztalcenie)

        elif wiek < 50:
            cechy.ruch -= 1
            cechy.wyglad -= 5
            punkty_do_odjecia = 5
            cechy.sila, cechy.kondycja, cechy.zrecznosc = cls.modyf_cech(
                punkty_do_odjecia, cechy.sila, cechy.kondycja, cechy.zrecznosc
            )
            for _ in range(2):
                cechy.wyksztalcenie += cls.test_rozwoju(cechy.wyksztalcenie)

        elif wiek < 60:
            cechy.ruch -= 2
            cechy.wyglad -= 10
            punkty_do_odjecia = 10
            cechy.sila, cechy.kondycja, cechy.zrecznosc = cls.modyf_cech(
                punkty_do_odjecia, cechy.sila, cechy.kondycja, cechy.zrecznosc
            )
            for _ in range(3):
                cechy.wyksztalcenie += cls.test_rozwoju(cechy.wyksztalcenie)

        elif wiek < 70:
            cechy.ruch -= 3
            cechy.wyglad -= 15
            punkty_do_odjecia = 20
            cechy.sila, cechy.kondycja, cechy.zrecznosc = cls.modyf_cech(
                punkty_do_odjecia, cechy.sila, cechy.kondycja, cechy.zrecznosc
            )
            for _ in range(4):
                cechy.wyksztalcenie += cls.test_rozwoju(cechy.wyksztalcenie)

        elif wiek < 80:
            cechy.ruch -= 4
            cechy.wyglad -= 20
            punkty_do_odjecia = 40
            cechy.sila, cechy.kondycja, cechy.zrecznosc = cls.modyf_cech(
                punkty_do_odjecia, cechy.sila, cechy.kondycja, cechy.zrecznosc
            )
            for _ in range(4):
                cechy.wyksztalcenie += cls.test_rozwoju(cechy.wyksztalcenie)

        else:
            cechy.ruch -= 5
            cechy.wyglad -= 25
            punkty_do_odjecia = 80
            cechy.sila, cechy.kondycja, cechy.zrecznosc = cls.modyf_cech(
                punkty_do_odjecia, cechy.sila, cechy.kondycja, cechy.zrecznosc
            )
            for _ in range(4):
                cechy.wyksztalcenie += cls.test_rozwoju(cechy.wyksztalcenie)

        cechy.save()
        return cechy
