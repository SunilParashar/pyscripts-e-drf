class polymor:
    def __init__(self, first_name="Sunil", last_name="Sharma"):
        self.first_name = first_name
        self.last_name = last_name

    # def sum(self, a, b):
    #     return a+b

    def __repr__(self):
        return f"My name is {self.first_name}  {self.last_name}"


class grade(polymor):
    def __init__(self, first_name, last_name, grade):
        super().__init__(first_name, last_name)
        self.grade = grade


def main():
    obj = polymor()
    print(obj)
    # print(obj.sum(1, 2))
    obj1 = grade("Aasdas", "sadasda", 123)
    print(obj1)


if __name__ == "__main__":
    main()
