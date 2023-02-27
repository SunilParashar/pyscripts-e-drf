def reverse(str) -> str:
    reversed_string = []
    for i in str:
        if i not in ('-', '*', '<'):
            reversed_string.insert(0, i)
    for i in str:
        if i in ('-', '*', '<'):
            pos = str.find(i)
            reversed_string.insert(pos, i)

    return ''.join(reversed_string)


if __name__ == '__main__':
    print(reverse('abc-de*fk<l'))
