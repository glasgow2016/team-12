from django.db import models

class tree(models.Model):
    treeName = models.CharField(max_length=128, default="")
    isTaken = models.BooleanField(default=False)

    def __unicode__(self):
        return self.treeName