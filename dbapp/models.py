from django.db import models

# Create your models here.
class Testlist(models.Model):
    id = models.IntegerField(primary_key=True)  # The composite primary key (id, name, age, mail) found, that is not supported. The first column is selected.
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    mail = models.CharField(max_length=20)
    prefecture_no = models.IntegerField()
    prefecture_name = models.CharField(max_length=255)
    prefecture_kana = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'testlist'
        unique_together = (('id', 'name', 'age', 'mail'),)

class PrefectureMst(models.Model):
     prefecture_no = models.IntegerField(primary_key=True)
     prefecture_name = models.CharField(max_length=255)
     prefecture_kana = models.CharField(max_length=255)
     regist_date = models.DateTimeField()
     update_date = models.DateTimeField()
     del_flg = models.IntegerField()

     class Meta:
        managed = False
        db_table = 'prefecture_mst'