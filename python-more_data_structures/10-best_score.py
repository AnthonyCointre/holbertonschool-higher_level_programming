#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = None
    best_student = None
    for key, value in a_dictionary.items():
        if max_score is None or value > max_score:
            max_score = value
            best_student = key
    return best_student
