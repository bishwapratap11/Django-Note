from django.db import models

# Create your models here.


class Notes(models.Model):
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return str(self.description)