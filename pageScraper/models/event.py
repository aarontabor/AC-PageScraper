from django.db import models
from pageScraper.models import Race


class Event(models.Model):
  race = models.ForeignKey(Race)

  name = models.CharField(max_length=32)

  def __unicode__(self):
    return u'%s' % self.name

  class Meta:
    app_label = 'pageScraper'
