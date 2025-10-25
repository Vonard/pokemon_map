from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True, verbose_name="Изображение покемона")

    def __str__(self):
        return '{}'.format(self.title)

class PokemonEntity(models.Model):
    Lat = models.FloatField()
    Lon = models.FloatField()