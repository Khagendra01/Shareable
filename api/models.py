from django.db import models
from pgvector.django import VectorField

class CustomUser(models.Model):
    pass



class Grave(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    other_Name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=15)
    is_alive = models.BooleanField()
    dob = models.DateTimeField()
    dod = models.DateTimeField(blank=True, null=True)
    voice_id = models.CharField(max_length=255, blank=True, null=True)

class GraveImages(models.Model):
    grave = models.ForeignKey(Grave, models.DO_NOTHING)
    image = models.URLField(max_length=255)

class LangchainPgEmbedding(models.Model):
    uuid = models.UUIDField(primary_key=True)
    embedding = VectorField(dimesions=1536) 
    document = models.CharField(blank=True, null=True)
    cmetadata = models.TextField(blank=True, null=True)
    custom_id = models.CharField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'langchain_pg_embedding'
