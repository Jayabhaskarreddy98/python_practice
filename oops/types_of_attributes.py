class Attribute:
    string = 'This is a class attribute'  # class attribute

    def method(self, string1):
        s = 'This is a local attribute'  # local
        self.string1 = string1  # instance / object

        print(f'{Attribute.string}')
        print(s)
        print(self.string1)

object = Attribute()

object.method('This is from object')