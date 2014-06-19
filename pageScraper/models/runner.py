from django.db import models


class Runner(models.Model):
  name = models.CharField(max_length=64)
  sex = models.CharField(max_length=1)
  city = models.CharField(max_length=128)
  province = models.CharField(max_length=32)

  def __unicode__(self):
    return u'%s' % (self.name)

  class Meta:
    app_label = 'pageScraper'
