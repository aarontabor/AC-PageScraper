from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from pageScraper.lib.findsOrCreatesRace import FindsOrCreatesRace

from pageScraper.models import Race
from pageScraper.forms.raceForm import RaceForm


def mapRace(request):
  if request.method == 'POST':
    form = RaceForm(request.POST)
    if form.is_valid():
      race = FindsOrCreatesRace().findOrCreate(form.cleaned_data)
      race.save()
      request.session['race_id'] = race.id
      return redirect(reverse('pageScraper:map_event'))
    else:
      return renderMapRace(request,form)
  else:
    form = RaceForm(initial={
      'name': request.session.get('name'),
      'location': request.session.get('location'),
      'raceDirector': request.session.get('raceDirector'),
      'date': request.session.get('date'),
    })
    return renderMapRace(request,form)

def renderMapRace(request, form):
  return render(request, 'mapRace.html', {
    'form': form,
  })


