from django.db import models

# Create your models here.

class NGO(models.Model):

    name = models.CharField(max_length=30)
    purpose = models.TextField()
    date_join = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
