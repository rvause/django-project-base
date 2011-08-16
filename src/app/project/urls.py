from django.contrib import admin

from django.conf.urls.defaults import *
from django.conf import settings


admin.autodiscover()


urlpatterns = patterns(
    '',

    url(r'^$', 'project.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)


if settings.DEBUG:
    from django.views.generic.simple import direct_to_template

    urlpatterns += patterns(
        '',

        url(
            r'^static/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root':  settings.MEDIA_ROOT, 'show_indexes': True}
        ),

        url(
            r'^robots.txt$',
            direct_to_template,
            {'template': 'robots.txt'},
            name='robots'
        ),
    )

