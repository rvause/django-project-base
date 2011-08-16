class Enum(object):

    def __init__(self, **kw):
        self.attrs = kw
        for key, value in kw.items():
            setattr(self, key, key)

    def __iter__(self):
        return iter(self.attrs.items())

