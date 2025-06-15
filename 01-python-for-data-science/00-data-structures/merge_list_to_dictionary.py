"""
Merge 2 list into Dictionary
Merge Lists to Dictionary

Design a Python function named merge_lists_to_dictionary to merge two lists into a dictionary where elements from the first list act as keys and elements from the second list act as values.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596161#overview

Parameters:

keys (List): A list of keys.

values (List): A list of values.

Returns:

A dictionary containing merged key-value pairs.

Example:

Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}

Input: keys = ['x', 'y', 'z'], values = [10, 20, 30]
Output: {'x': 10, 'y': 20, 'z': 30}

"""

def merge_lists_to_dictionary(keys, values):
    merge_dict = {}
    if len(keys) != len(values):
        return False
    for i in range(len(keys)):
        merge_dict[keys[i]] = values[i]
    return merge_dict
if __name__ =="__main__":
    sample_input1 = ['a','b','c']
    sample_input2 = [1,2,3]
    print("Output : ",merge_lists_to_dictionary(sample_input1,sample_input2))