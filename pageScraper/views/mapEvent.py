from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from pageScraper.lib.findsOrCreatesObject import FindsOrCreatesObject

from pageScraper.models import Event, Race
from pageScraper.forms.eventForm import EventForm


def mapEvent(request):
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      toSubmit = form.cleaned_data

      race = Race.objects.get(pk=request.session['race_id'])
      toSubmit['race'] = race

      event = FindsOrCreatesObject(Event).findOrCreate(toSubmit)
      event.save()
      request.session['event_id'] = event.id

      return redirect(reverse('pageScraper:map_runners'))
    else:
      return renderMapEvent(request, form)
  else:
    form = EventForm(initial={
      'name': request.session.get('eventName'),
    })
    return renderMapEvent(request, form)

def renderMapEvent(request, form):
    return render(request, 'mapEvent.html', {
      'form': form,
    })


