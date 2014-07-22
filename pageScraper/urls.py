from pageScraper import views
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'atlanticChipPageScraper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^specify', views.specify, name='specify'),
    url(r'^map_headers', views.mapHeaders, name='map_headers'),
    url(r'^confirm', views.confirm, name='confirm'),
)
