def get_split_input(dtype=None):
    l = input().rstrip().split()
    if dtype is None:
        return l
    elif isinstance(dtype, type):
        return map(dtype, l)
    else:
        return (dtype[index](l[index]) for index in len(l))

