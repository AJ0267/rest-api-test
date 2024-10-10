from django.db import models

# Create your models here.
class Quote(models.Model):
    def __str__(self):
        name = self.quote
        return name
    id = models.AutoField(primary_key=True)
    quote = models.CharField(max_length=500)
