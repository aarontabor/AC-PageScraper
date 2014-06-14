from django.db import models


class Runner(models.Model):
  class Meta:
    app_label = 'pageScraper'
  firstName = models.CharField(max_length=30)
  lastName = models.CharField(max_length=30)
