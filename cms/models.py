from django.db import models

class Schema(models.Model):
    parent_id = models.BigIntegerField
    name = models.CharField(max_length=255, verbose_name="Nombre")
    alias = models.CharField(max_length=50, verbose_name="Alias")
    fields = models.JSONField
    active = models.BooleanField

    def __str__(self):
        return self.name
