"""
Merge Dictionaries with Common Keys
Problem Description

Merge Dictionaries with Overlapping Keys

Design a Python function named merge_dicts_with_overlapping_keys that merges multiple dictionaries into a single dictionary. If a key appears in more than one dictionary, sum up their values.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596169#overview

Parameters:

dicts (list): A list of dictionaries where keys might overlap.

Returns:

A single dictionary where values for overlapping keys are summed.

Example:

Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
Output: {'a': 1, 'b': 5, 'c': 9, 'd': 6}

Input: [{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]
Output: {'x': 70, 'y': 50, 'z': 90}
"""
def merge_dicts_with_overlapping_keys(dicts):
    res_dict = {}
    for element in dicts:
        for keys,value in element.items():
            if keys not in res_dict:
                res_dict[keys] = value
            else:
                res_dict[keys] += value
    return res_dict
if __name__ == "__main__":
    sample_input = [{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]
    print("Output : ",merge_dicts_with_overlapping_keys(sample_input))