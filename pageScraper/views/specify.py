from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from pageScraper.lib.scrapesPages import ScrapesPages

from pageScraper.forms.specifyForm import SpecifyForm


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
      request.session['rawResults'] = scraper.rawResultText()
      return redirect(reverse('pageScraper:map_race'))
    else:
      return renderSpecify(request, form)
  else:
    form = SpecifyForm()
    return renderSpecify(request, form)

def renderSpecify(request, form):
  return render(request, 'specify.html', {
    'form': form,
  })

