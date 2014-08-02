from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from pageScraper.lib.buildsObjectsFromResultList import BuildsObjectsFromResultList
from pageScraper.lib.findsOrCreatesObject import FindsOrCreatesObject

from pageScraper.models import Runner
from pageScraper.forms.runnerForm import RunnerForm


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
      return redirect(reverse('pageScraper:map_results'))
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
    'headers': request.session.get('headers'),
    'title': 'Map Runner Data',
  })


