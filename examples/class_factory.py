class SomeBaseClass(object):
    def say_hello(self):
        print("Hi.")

class SomeOtherBaseClass(object):
    def say_hello(self):
        print("Yo.")

def class_factory(BaseClass):
    class SpecificClass(BaseClass):
        def __init__(self, *args, **kwargs):
            super(SpecificClass, self).__init__(*args, **kwargs)
    return SpecificClass

one = class_factory(SomeBaseClass)()
two = class_factory(SomeOtherBaseClass)()

for thing in (one,two):
    thing.say_hello()