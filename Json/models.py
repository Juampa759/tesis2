from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class person(models.Model):
    User = models.ForeignKey(User, verbose_name="Usuario", on_delete= models.CASCADE)
    pregunta = models.IntegerField()
    score = models.IntegerField()

class pregunta(models.Model):
    pregunta = models.CharField(max_length=500)
    resA = models.CharField(max_length=200)
    resB = models.CharField(max_length=200)
    resC = models.CharField(max_length=200)
    resD = models.CharField(max_length=200)

class RespuestaUsu(models.Model):
    User = models.ForeignKey(User, verbose_name="Usuario", on_delete= models.CASCADE)
    Pregunta = models.ForeignKey(pregunta, verbose_name="Pregunta", on_delete= models.CASCADE)
    respuesta = models.CharField(max_length=200)
