import logging

class Observable(object):

    def __init__(self, value = None):
        object.__init__(self)

        self._previousValue = None
        self._value = value
        self._callbacks = []

    def __repr__(self):
        return self._value.__repr__()

    def __str__(self):
        return self._value.__str__()

    def _onChangeHandler(self):
        try:
            for index, callback in enumerate(self._callbacks):
                callback(self._value, self._previousValue)
        except Exception as e:
            logging.error(e.message)

    def set(self, value):
        self._previousValue = self._value
        self._value = value

        self._onChangeHandler()

        return self

    def subscribe(self, callback):
        if hasattr(callback, '__call__'):
            if not callback in self._callbacks:
                self._callbacks.append(callback)

        return self

    def unsubscribe(self, callback):
        if hasattr(callback, '__call__'):
            try:
                index = self._callbacks.index(callback)
            except ValueError as e:
                logging.error(e.message)
            else:
                del self._callbacks[index]

        return self

class ObservableList(Observable):

    def __init__(self, value = []):
        Observable.__init__(self, value)

    def __getattr__(self, name = None):
        if name in dir(self._value):
            return lambda value: self._modifyList(name, value)

        Observable.__getattr__(self, name)

    def _modifyList(self, name, value):
        self._previousValue = [] + self._value

        getattr(self._value, name)(value)

        self._onChangeHandler()
