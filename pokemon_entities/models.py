import datetime

from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, verbose_name="Изображение покемона")

    def __str__(self):
        return '{}'.format(self.title)

class PokemonEntity(models.Model):
    id = models.AutoField(primary_key=True)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
    appeared_at = models.DateTimeField(verbose_name="Время появления покемона", default=datetime.datetime.now)
    disappeared_at = models.DateTimeField(verbose_name="Время исчезновения покемона", default=None)
    level = models.IntegerField(verbose_name="Уровень", default=0)
    health = models.IntegerField(verbose_name="Здоровье", blank=True, null=True)
    strength = models.IntegerField(verbose_name="Атака", blank=True, null=True)
    defence = models.IntegerField(verbose_name="Защита", blank=True, null=True)
    stamina = models.IntegerField(verbose_name="Выносливость", blank=True, null=True)