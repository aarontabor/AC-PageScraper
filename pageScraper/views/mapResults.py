from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from pageScraper.lib.buildsObjectsFromResultList import BuildsObjectsFromResultList
from pageScraper.lib.findsOrCreatesResult import FindsOrCreatesResult

from pageScraper.models import Result, Event, Runner
from pageScraper.forms.resultForm import ResultForm

import copy


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

def filterPopulatedData(allData):
  populatedTuples = filter(
      lambda (x,y) : y is not None,
      allData.items())
  return dict(populatedTuples)

def renderResultForm(request, form):
  return render(request, 'mapChoices.html', {
      'form': form,
      'headers': request.session.get('headers'),
      'title': 'Map Result Data',
    })


