from django.db import models


class Runner(models.Model):
  class Meta:
    app_label = 'pageScraper'
  firstName = models.CharField(max_length=30)
  lastName = models.CharField(max_length=30)

  def __unicode__(self):
    return u'<Runner: "%s, %s">' % (self.lastName, self.firstName)
