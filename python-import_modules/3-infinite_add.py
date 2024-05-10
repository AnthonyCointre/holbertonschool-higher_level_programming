#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(f"0")
    else:
        result = 0
        for arg in sys.argv[1:]:
            result += int(arg)
        print("{}".format(result))
