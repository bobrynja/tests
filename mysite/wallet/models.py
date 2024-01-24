from django.db import models


class Wallet(models.Model):
    balance_RUB = models.FloatField(default=0)
    balance_USD = models.FloatField(default=0)
    id_person = models.IntegerField()

class Operation(models.Model):
    type = models.CharField(max_length=20)
    money = models.FloatField(default=0)
    unit = models.CharField(max_length=3, default='RUB')
    id_wallet_1 = models.IntegerField()
    id_wallet_2 = models.IntegerField()

