from django.db import models

class OverallScopus(models.Model):
    scholarlyOutputOverall = models.TextField(blank=True)
    authorsOverall = models.TextField(blank=True)
    citationsOverall = models.TextField(blank=True)
    citationsPerPubOverall = models.TextField(blank=True)
    createdAtFirst = models.DateTimeField(auto_now_add=True)
    updatedAtFirst = models.DateTimeField(auto_now=True)

    #def __str__(self):




