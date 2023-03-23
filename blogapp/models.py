# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Post(models.Model):
    idpost = models.OneToOneField('Tema', models.DO_NOTHING, db_column='idpost', primary_key=True)
    nome_post = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'

    def __str__(self):
        return self.nome_post


class Tema(models.Model):
    idtema = models.IntegerField(primary_key=True)
    nome_tema = models.CharField(max_length=45)
    foto_tema = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tema'
    def __str__(self):
        return self.nome_tema
