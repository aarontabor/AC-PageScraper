from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from pageScraper.forms.specifyForm import SpecifyForm
from pageScraper.forms.raceForm import RaceForm
from pageScraper.forms.eventForm import EventForm
from pageScraper.forms.runnerForm import RunnerForm
from pageScraper.forms.resultForm import ResultForm
from pageScraper.lib.scrapesPages import ScrapesPages
from pageScraper.lib.findsOrCreatesObject import FindsOrCreatesObject
from pageScraper.lib.findsOrCreatesResult import FindsOrCreatesResult
from pageScraper.lib.buildsObjectsFromResultList import BuildsObjectsFromResultList
from pageScraper.models import Race, Event, Runner, Result
import copy


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

def mapRunners(request):
  if request.method == 'POST':
    form = RunnerForm(request.POST)
    if form.is_valid():
      populatedFields = filterPopulatedData(form.cleaned_data)
      runners = BuildsObjectsFromResultList(FindsOrCreatesObject(Runner)).build(
          request.session.get('results'), 
          populatedFields)
      runner_ids = []
      for runner in runners:
        runner.save()
        runner_ids.append(runner.id)
      request.session['runner_ids'] = runner_ids
      return redirect(reverse('pageScraper:confirm'))
    else:
      return renderMapRunners(request, form)
  else:
    form = RunnerForm()
    return renderMapRunners(request, form)

def filterPopulatedData(allData):
  populatedTuples = filter(
      lambda (x,y) : y is not None,
      allData.items())
  return dict(populatedTuples)

def renderMapRunners(request, form):
  form = RunnerForm()
  return render(request, 'mapChoices.html', {
    'form': form,
    'headers': request.session.get('headers')
  })

def mapResults(request):
  if request.method == 'POST':
    form = ResultForm(request.POST)
    if form.is_valid():
      populatedFields = filterPopulatedData(form.cleaned_data)
      augmentedResults = copy.deepcopy(request.session.get('results'))

      runner_ids = request.session.get('runner_ids')
      populatedFields['runner'] = len(augmentedResults[0])
      for index, result in enumerate(augmentedResults):
        result.append(Runner.objects.get(pk=runner_ids[index]))

      event_id = request.session.get('event_id')
      event = Event.objects.get(pk=event_id)
      populatedFields['event'] = len(augmentedResults[0])
      for result in augmentedResults:
        result.append(event)

      resultObjects = BuildsObjectsFromResultList(FindsOrCreatesResult()).build(
          augmentedResults,
          populatedFields)

      result_ids = []
      for result in resultObjects:
        result.save()
        result_ids.append(result.id)

      request.session['result_ids'] = result_ids
      return redirect(reverse('pageScraper:confirm'))
    else:
      return renderResultForm(request, form)
  else:
    form = ResultForm()
    return renderResultForm(request, form)

def renderResultForm(request, form):
  return render(request, 'mapChoices.html', {
      'form': form,
      'headers': request.session.get('headers'),
    })

def confirm(request):
  return render(request, 'confirm.html')
