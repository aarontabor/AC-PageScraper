from django.forms import ModelForm
from pageScraper.models import Event


class EventForm(ModelForm):
  class Meta:
    model = Event
    exclude = ('race',)
