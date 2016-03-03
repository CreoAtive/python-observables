# python-observables

A simple package to create observable variables and observable lists.

## Usage

### Observable(value)

Create an instance of Observable with an initial value and add onChangeCallbacks via the subscribe method. Use the set method to change the value. All subscribed callbacks will be executed with new_value and old_value as arguments.

**example**

```python
from observables import Observable

def onChangeCallback(new_value, old_value):
    print new_value, old_value

new_observable = Observable('Foo')

new_observable.subscribe(onChangeCallback)

print new_observable # will print "Foo"

new_observable.set('Bar') # will execute the callback "onChangeCallback" and print "Bar", "Foo"

new_observable.unsubscribe(onChangeCallback) # will remove the callback

print new_observable # will print "Bar"
```

### ObservableList(list)

Create an instance of ObservableList with an initial list and add onChangeCallbacks via the subscribe method. Use default list methods to modify the list. All subscribed callbacks will be executed with new_value and old_value as arguments.

**example**

```python
from observables import ObservableList

def onChangeCallback(new_value, old_value):
    print new_value, old_value

new_observable_list = ObservableList(range(5))

new_observable_list.subscribe(onChangeCallback)

print new_observable_list # will print "[0, 1, 2, 3, 4]"

new_observable_list.append(5) # will execute the callback "onChangeCallback" and print "[0, 1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4]"

new_observable_list.unsubscribe(onChangeCallback) # will remove the callback

print new_observable_list # will print "[0, 1, 2, 3, 4, 5]"
```
