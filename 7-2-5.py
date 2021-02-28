from string import printable


def sequence_del(my_str):
    for c in printable:
        while (c * 2) in my_str:
            my_str = my_str.replace(c * 2, c)

    return my_str
