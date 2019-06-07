from django.db import models
from django.utils import timezone

class equation(models.Model):
    chiffre1 = models.CharField(max_length=100)
    operation = models.CharField(max_length=100)
    chiffre2 = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")

    class Meta:
        ordering = ['date']

    def __str__(self):
    	return self.chiffre1 + " " + self.operation + " " + self.chiffre2