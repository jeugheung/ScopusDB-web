from django.db import models

class Researchers(models.Model):
    number = models.IntegerField(db_column='number', blank=False, default=2000)
    name = models.CharField(db_column='name', max_length=100, blank=False)
    sch_output = models.IntegerField(db_column='sch_output',blank=False, default=2000)
    year = models.IntegerField(db_column='year',blank=False, default=2000)
    citations = models.IntegerField(db_column='citations',blank=False, default=2000)
    h_index = models.IntegerField(db_column='h_index', blank=False, default=2000)
    class Meta:
        db_table = 'researchers'
        verbose_name = 'Researchers'
        verbose_name_plural = 'Researchers'
        ordering = ['number']
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name



