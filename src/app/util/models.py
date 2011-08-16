from django.db import models

from django.contrib.sites.models import Site


class GenericManager(models.Manager):
    '''Filter query set by given selectors.'''
    def __init__(self, **kwargs):
        super(GenericManager, self).__init__()
        self.selectors = kwargs

    def get_query_set(self):
        return super(GenericManager, self).get_query_set().filter(**self.selectors)


class GetUrlMixin(object):
    '''Avoids need to define all URL-related model methods.
    Just define get_url_path method that returns absolute path
    (but not absolute URL).

    '''

    def get_absolute_url(self):  # for backwards compatibility.
        return self.get_url_path()

    def get_url(self):
        '''Build absolute URL basing on current Site.'''
        return 'http://%s%s' % (
            Site.objects.get_current().domain,
            self.get_url_path(),
        )


def make_q_cls(*fields, **kw):
    replicate = kw.get('replicate', True)
    _fields = fields

    def _q(field, value):
        return models.Q(**{field + '__icontains': value})

    def make_q_instance(*values):
        q = _q(_fields[0], values[0])

        if replicate and len(values) == 1:
            values = values * len(fields)

        for field, value in zip(_fields[1:], values[1:]):
            q |= _q(field, value)

        return q

    return make_q_instance

