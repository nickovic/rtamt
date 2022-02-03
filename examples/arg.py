def funcA(reserve, left, right):
    print(reserve)
    print(left)
    print(right)

def funcB(reserve, *args, **kwargs):
    print(reserve)
    print(args[0])
    print('')
    funcA(reserve, *args, **kwargs)


funcB('hoge', 'foo', 'bar')