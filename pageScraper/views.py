from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from pageScraper.forms.specifyForm import SpecifyForm
from pageScraper.forms.raceForm import RaceForm
from pageScraper.forms.eventForm import EventForm
from pageScraper.lib.scrapesPages import ScrapesPages
from pageScraper.lib.findsOrCreatesObject import FindsOrCreatesObject
from pageScraper.models import Race, Event


# Create your views here.
def specify(request):
  if request.method == 'POST':
    form = SpecifyForm(request.POST)
    if form.is_valid():
      url = form.cleaned_data['url']
      scraper = ScrapesPages(url)
      request.session['headers'] = scraper.scrapeHeaders()
      request.session['results'] = scraper.scrapeResults()
      request.session['raceName'] = scraper.scrapeRaceName()
      request.session['eventName'] = scraper.scrapeEventName()
      request.session['location'] = scraper.scrapeLocation()
      request.session['date'] = scraper.scrapeDate()
      request.session['raceDirector'] = scraper.scrapeRaceDirector()
      return redirect(reverse('pageScraper:confirm'))
    else:
      return renderSpecify(request, form)
  else:
    form = SpecifyForm()
    return renderSpecify(request, form)

def renderSpecify(request, form):
  return render(request, 'specify.html', {
    'form': form,
  })


def mapRace(request):
  if request.method == 'POST':
    form = RaceForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      location = form.cleaned_data['location']
      raceDirector = form.cleaned_data['raceDirector']
      date = form.cleaned_data['date']

      race = FindsOrCreatesObject(Race).findOrCreate({
        'name': name,
        'location': location,
        'raceDirector': raceDirector,
        'date': date,
      })
      race.save()
      request.session['race_id'] = race.id
      return redirect(reverse('pageScraper:confirm'))
    else:
      return renderMapEvent(request,form)
  else:
    form = RaceForm(initial={
      'name': request.session.get('name'),
      'location': request.session.get('location'),
      'raceDirector': request.session.get('raceDirector'),
      'date': request.session.get('date'),
    })
    return renderMapEvent(request,form)

def renderMapEvent(request, form):
  return render(request, 'mapRace.html', {
    'form': form,
  })

def mapEvent(request):
  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      name = form.cleaned_data['name']
      race = Race.objects.get(pk=request.session['race_id'])

      event = FindsOrCreatesObject(Event).findOrCreate({
        'name': name,
        'race': race,
      })
      event.save()
      request.session['event_id'] = event.id

      return redirect(reverse('pageScraper:confirm'))
    else:
      return renderMapEvent(request, form)
  else:
    form = EventForm(initial={
      'name': request.session.get('eventName'),
      'race': request.session.get('race'),
    })
    return renderMapEvent(request, form)

def renderMapEvent(request, form):
    return render(request, 'mapEvent.html', {
      'form': form,
    })

def mapHeaders(request):
  return render(request, 'mapHeaders.html')

def confirm(request):
  return render(request, 'confirm.html')
