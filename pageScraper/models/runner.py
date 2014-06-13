from django.db import models


class Runner(models.Model):
  class Meta:
    app_label = 'pageScraper'
  first_name = models.CharField(max_length=30)
