from django.forms import ModelForm
from pageScraper.models import Race


class RaceForm(ModelForm):
  class Meta:
    model = Race
    fields = '__all__'
