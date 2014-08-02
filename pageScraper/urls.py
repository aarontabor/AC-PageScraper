from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'atlanticChipPageScraper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^specify', 'pageScraper.views.specify.specify', name='specify'),
    url(r'^map_race', 'pageScraper.views.mapRace.mapRace', name='map_race'),
    url(r'^map_event', 'pageScraper.views.mapEvent.mapEvent', name='map_event'),
    url(r'^map_runners', 'pageScraper.views.mapRunners.mapRunners', name='map_runners'),
    url(r'^map_results', 'pageScraper.views.mapResults.mapResults', name='map_results'),
    url(r'^confirm', 'pageScraper.views.confirm.confirm', name='confirm'),
)
