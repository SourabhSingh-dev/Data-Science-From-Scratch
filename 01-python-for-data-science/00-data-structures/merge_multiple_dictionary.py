"""
Merge Multiple Dictionary
Merge Three Dictionaries

Design a Python function named merge_three_dictionaries to merge exactly three dictionaries into one.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596163#overview

Parameters:

dict1 (Dictionary): The first dictionary to be merged.

dict2 (Dictionary): The second dictionary to be merged.

dict3 (Dictionary): The third dictionary to be merged.

Returns:

A single dictionary containing all key-value pairs from the three input dictionaries.

Example:

Input: ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

Input: ({'x': 10, 'y': 20}, {'z': 30}, {'a': 40, 'b': 50})
Output: {'x': 10, 'y': 20, 'z': 30, 'a': 40, 'b': 50}
"""
def merge_three_dictionaries(dict1, dict2, dict3):
    final_dict = {}
    # for keys,values in dict1.items():
    #     final_dict[keys] = values
    # this first loops can be removed...we can directly copy and paste the dict1 into result 
    final_dict = dict1.copy()
    for keys,values in dict2.items():
        final_dict[keys] = values
    for keys,values in dict3.items():
        final_dict[keys] = values
    return final_dict
if __name__ == "__main__":
    sample_input1,sample_input2,sample_input3 = {'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}
    print("Output : ",merge_three_dictionaries(sample_input1,sample_input2,sample_input3))