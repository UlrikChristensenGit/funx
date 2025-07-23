class Composite(type):

    def __instancecheck__(self, instance):
        name_equals = (instance.__class__.__name__ == self.__name__)
        if self.Domain == ...:
            domain_equals = True
        else:
            domain_equals = issubclass(instance.Domain, self.Domain)
        return name_equals & domain_equals

    def __new__(cls, name, bases, dct):
        parent = super()

        if "Domain" not in dct:
            raise TypeError("Composite classes must define a 'Domain' attribute")

        class Factory:

            def __getitem__(self, key):

                x = parent.__new__(cls, name, bases, dct)

                setattr(x, 'Domain', key)

                return x

        return Factory()
