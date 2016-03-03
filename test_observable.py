import logging
logging.basicConfig(level=logging.DEBUG)

from observables import Observable, ObservableList

def observableTest():
    def callback_a(new_value, old_value):
        logging.info('value is "{new_value}" and was "{old_value}"'.format(new_value = new_value, old_value = old_value))

    new_observable = Observable('hello world')

    new_observable.subscribe(callback_a)

    new_observable.set('foobar').set('wumbada')

    new_observable.set('hello again')

    print new_observable

def observableListTest():
    def callback_a(new_value, old_value):
        logging.info('value is "{new_value}" and was "{old_value}"'.format(new_value = new_value, old_value = old_value))

    new_observable_list = ObservableList(range(5))

    new_observable_list.subscribe(callback_a)

    new_observable_list.append(5)

    new_observable_list.pop(1)

    new_observable_list.remove(2)

    print new_observable_list

def main():
    observableTest()

    observableListTest()

if __name__ == '__main__':
    main()
