from django.db import models


class Race(models.Model):
  name = models.CharField(max_length=128)
  location = models.CharField(max_length=128)
  raceDirector = models.CharField(max_length=64)
  date = models.DateField()

  def __unicode__(self):
    return u'%s' % self.name

  class Meta:
    app_label = 'pageScraper'
