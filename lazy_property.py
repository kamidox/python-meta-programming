# -*- coding=utf8 -*-

class lazy_property(object):
    """A @property that is only evaluated once."""

    def __init__(self, deferred):
        print('{0}.{1} ENTER'.format(self.__class__.__name__, '__init__'))
        self._deferred = deferred
        self.__doc__ = deferred.__doc__
        print('{0}.{1} EXIT'.format(self.__class__.__name__, '__init__'))

    def __get__(self, obj, cls):
        print('{0}.{1} ENTER'.format(self.__class__.__name__, '__get__'))
        if obj is None:
            return self
        # This is the key of lazy init. It call the function to get a value.
        value = self._deferred(obj)
        # Then, set the value to obj's property with exactly the same name of the init function.
        setattr(obj, self._deferred.__name__, value)
        print('{0}.{1} EXIT'.format(self.__class__.__name__, '__get__'))
        return value


class Signal(object):
    """A notification emitter."""

    @lazy_property
    def receiver_connected(self):
        """ Define a lazy init property

        This is defined as a function. After init, it become a property.

        """
        print('{0}.{1} ENTER'.format(self.__class__.__name__, 'receiver_connected'))
        return Signal(doc="Emitted after a receiver connects.")
        print('{0}.{1} EXIT'.format(self.__class__.__name__, 'receiver_connected'))

    def __init__(self, doc=None):
        print('{0}.{1} ENTER'.format(self.__class__.__name__, '__init__'))
        if doc:
            self.__doc__ = doc
        print('{0}.{1} EXIT'.format(self.__class__.__name__, '__init__'))

if __name__ == '__main__':
    print('create Signal instance')
    s = Signal('test Signal')
    print('id(s)={0} type(s)={1}'.format(id(s), type(s)))
    print('access receiver_connected from instance')
    s2 = s.receiver_connected
    print('id(s2)={0} type(s2)={1}'.format(id(s2), type(s2)))
    print('access receiver_connected from instance again')
    s3 = s.receiver_connected
    print('id(s3)={0} type(s3)={1}'.format(id(s3), type(s3)))
    print('access receiver_connected from Signal Class')
    s4 = Signal.receiver_connected
    print('id(s4)={0} type(s4)={1}'.format(id(s4), type(s4)))

