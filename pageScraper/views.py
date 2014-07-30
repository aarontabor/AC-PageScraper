from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from pageScraper.forms.specifyForm import SpecifyForm
from pageScraper.lib.scrapesPages import ScrapesPages


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
      return render(request, 'specify.html', {
        'form': form
      })
  else:
    form = SpecifyForm()
    return render(request, 'specify.html', {
      'form': form,
    })

def mapHeaders(request):
  return render(request, 'mapHeaders.html')

def confirm(request):
  return render(request, 'confirm.html')
