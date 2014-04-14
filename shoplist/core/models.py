from django.db import models


class Shoplist(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return "{} ({} items)".format(self.name,
                                      self.shopitem_set.count())


# Create your models here.
class Shopitem(models.Model):
    name = models.CharField(max_length=200)
    shoplist = models.ForeignKey(Shoplist)

    def __unicode__(self):
        return self.name
