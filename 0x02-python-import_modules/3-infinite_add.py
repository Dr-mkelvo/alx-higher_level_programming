#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_counter = len(argv)
    index = 1
    result = 0
    while index <= argv_counter:
        results += int(sys.argv[index])
        index += 1
    print("{:d}".format(results))
