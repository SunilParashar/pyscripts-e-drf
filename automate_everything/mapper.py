from functools import reduce


def square(x):
    return x*x


def main():
    my_list = [1, 2, 3, 4, 5, 6, 7]
    # MAP
    squared_values = map(square, my_list)
    print(list(squared_values))
    print(list(map((lambda x: x*x), my_list)))
    # REDUCE
    print(reduce((lambda x, y: x+y), my_list))
    # FILTER
    print(list(filter((lambda x: x % 2 == 0), my_list)))


if __name__ == '__main__':
    main()
