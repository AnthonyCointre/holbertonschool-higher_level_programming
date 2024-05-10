#!/usr/bin/python3
if __name__ == "__main__":
    """ Import names from hidden_4.pyc """
    import hidden_4
    names = []
    for name in dir(hidden_4):
        if not name[0:2] == "__":
            names.append(name)
    names.sort()
    for name in names:
        print(name)
