from django.db import models

class Currency(models.Model):
    pair = models.CharField(max_length=20)
    bid = models.FloatField()
    ask = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    change = models.CharField(max_length=20)
    change_p = models.CharField(max_length=20)
    time = models.TimeField()

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.pair
            