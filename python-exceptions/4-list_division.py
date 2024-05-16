#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else None
            b = my_list_2[i] if i < len(my_list_2) else None
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("wrong type")
            if b == 0:
                raise ZeroDivisionError("division by 0")
            result.append(a / b)
        except TypeError as e:
            print(e)
            result.append(0)
        except ZeroDivisionError as e:
            print(e)
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass
    return result
