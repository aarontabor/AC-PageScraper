from django.db import models
from pageScraper.models import Runner
from pageScraper.models import Event


class Result(models.Model):
  runner = models.ForeignKey(Runner)
  event = models.ForeignKey(Event)

  position = models.IntegerField()
  bib = models.IntegerField()
  gunTime = models.CharField(max_length=32)
  chipTime = models.CharField(max_length=32)
  division = models.CharField(max_length=32)

  def __unicode__(self):
    return u'%s-%s' % (self.position, self.bib)

  class Meta:
    app_label = 'pageScraper'
