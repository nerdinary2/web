from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Figures(models.Model):
    manid = models.TextField(blank=True, primary_key=True)
    url = models.TextField(blank=True, null=True)
    korname = models.TextField(blank=True, null=True)
    chnname = models.TextField(blank=True, null=True)
    korbon = models.TextField(blank=True, null=True)
    chnbon = models.TextField(blank=True, null=True)
    birth = models.IntegerField(blank=True, null=True)
    death = models.IntegerField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    uci = models.TextField(blank=True, null=True)
    examkey = models.TextField(blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    deleted = models.IntegerField(null=False)
    checked = models.IntegerField(null=False)

    class Meta:
        db_table = "figures"

    def __iter__(self):
        for field in self._meta.fields:
            yield (field.verbose_name, field.value_to_string(self))


class Records(models.Model):
    manid = models.TextField(blank=True, null=True)
    officelevel = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    paraid = models.TextField(blank=True, null=True)
    jobid = models.BigIntegerField(blank=True, null=True)
    level = models.FloatField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    rdate = models.BigIntegerField(blank=True, null=True)
    korname = models.TextField(blank=True, null=True)
    chnname = models.TextField(blank=True, null=True)
    gye = models.TextField(blank=True, null=True)
    sa = models.TextField(blank=True, null=True)
    jik = models.TextField(blank=True, null=True)
    impossible = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    nation = models.TextField(blank=True, null=True)
    class Meta:
        db_table = "records"


class Bangmok(models.Model):
    personid = models.TextField(blank=True, primary_key=True)
    url = models.TextField(blank=True, null=True)
    relatives = models.TextField(blank=True, null=True)
    chnname = models.TextField(blank=True, null=True)
    residence = models.TextField(blank=True, null=True)
    affilliation = models.TextField(blank=True, null=True)
    king = models.TextField(blank=True, null=True)
    korname = models.TextField(blank=True, null=True)
    class_field = models.FloatField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    year_of_pass = models.FloatField(blank=True, null=True)
    rank = models.FloatField(blank=True, null=True)
    exam_type = models.TextField(blank=True, null=True)
    family_clan = models.TextField(blank=True, null=True)
    birth = models.FloatField(blank=True, null=True)
    death = models.FloatField(blank=True, null=True)
    clan2 = models.TextField(blank=True, null=True)
    plastic = models.FloatField(blank=True, null=True)
    age_of_pass = models.FloatField(blank=True, null=True)
    career_length = models.FloatField(blank=True, null=True)
    class Meta:
        db_table = "bangmok"



class Article(models.Model):
    url = models.TextField(blank=True, primary_key=True)
    king = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    chinese = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    book = models.TextField(blank=True, null=True)
    nameid = models.TextField(blank=True, null=True)
    placeid = models.TextField(blank=True, null=True)
    bookid = models.TextField(blank=True, null=True)
    korean = models.TextField(blank=True, null=True)
    soldate = models.TextField(blank=True, null=True)
    rdate = models.BigIntegerField(blank=True, null=True)
    paragraph = models.TextField(blank=True, null=True)
    class Meta:
        db_table = "article"