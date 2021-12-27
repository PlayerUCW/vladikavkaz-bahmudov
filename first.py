def my():
    a = 'M'
    b = 'y'
    return a + b


def first():
    return 'first '


def git_repo(a, b):
    return ''.join(a) + '-' + repo(b.split('Z'))


def repo(a):
    return a[0] + a[1] + a[2] + a[3]


def main():
    a = ['i', 't']
    print(my() + ' ' + first() + git_repo(['g', *a], 'rZeZpZo'))


if __name__ == '__main__':
    main()