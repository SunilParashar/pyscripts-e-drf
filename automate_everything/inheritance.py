class TestClass:
    def sum(self, x, y):
        return x+y


class TestClass1:
    def div(self, x, y):
        return x/y


class TestClass2(TestClass):
    def subtract(self, x, y):
        return x-y


class TestClass3(TestClass1, TestClass2):
    def multiply(self, x, y):
        return x*y


class TestClass4(TestClass2):
    def mod(self, x, y):
        return x % y


def main():
    test = TestClass2()
    test2 = TestClass3()
    test4 = TestClass4()
    print(test.sum(3, 4))
    print(test.subtract(13, 4))
    print(test2.multiply(3, 4))
    print(test2.div(13, 4))
    print(test4.mod(13, 4))


if __name__ == '__main__':
    main()
