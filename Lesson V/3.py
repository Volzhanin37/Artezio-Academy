class Observable(object):

    def __init__(self, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

    def __str__(self):
        public_attributes = []
        for key in self.__dict__:
            if not key.startswith('_'):
                public_attributes.append(key + '=' + str(self.__dict__[key]))

        return (str(self.__class__.__name__) +
                '(' + ','.join(public_attributes) + ')')


class X(Observable):
    pass


# x = X(foo=1, bar="Test", _barr='hidden', baz=(5, 6))
# print(x.foo)
# print(x.bar)
# print(x._barr)
# print(x)
