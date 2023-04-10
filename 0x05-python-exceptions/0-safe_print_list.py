#!/usr/bin/python3


# def safe_print_list(my_list=[], x=0):
#     total = 0
#     for i in range(x):
#         try:
#             print("{}".format(my_list[i]), end="")
#             total += 1
#         except IndexError:
#             break
#     print("")
#     return (total)


def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        while counter < x:
            print(my_list[counter], end='')
            counter += 1
    except IndexError:
        pass
    finally:
        print('\n')
    return counter