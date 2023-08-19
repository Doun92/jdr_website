from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Scénario(models.Model):
    titre = models.CharField(max_length=50)
    description = RichTextField()

    def __str__(self):
        return self.titre

class Acte(models.Model):
    scenario = models.ForeignKey(Scénario, on_delete= models.CASCADE)
    titre = models.CharField(max_length=50)
    description = RichTextField()
    numero = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.titre