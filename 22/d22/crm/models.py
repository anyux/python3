from django.db import models

# Create your models here.

class Depart(models.Model):

    title = models.CharField(verbose_name="部门名称",max_length=32)

    def __str__(self):
        return self.title