#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(f"0 arguments.")
    else:
        count = len(sys.argv) - 1
        id = 1
        if len(sys.argv) == 2:
            print("{} argument:".format(count))
        else:
            print("{} arguments:".format(count))
        for arg in sys.argv[1:]:
            print("{}: {}".format(id, arg))
            id += 1
