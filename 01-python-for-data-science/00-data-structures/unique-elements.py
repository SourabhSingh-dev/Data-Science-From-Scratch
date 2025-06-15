"""

Check if all elements in a List are Unique
Check if All Elements in a List are Unique

You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False.

Link :  https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596147#overview

Parameters:

lst (List of integers): The list of integers to check for uniqueness.

Returns:

A boolean value True if all elements in the list are unique, False otherwise.

Example:

Input: lst = [1, 2, 3, 4, 5]
Output: True

Input: lst = [1, 2, 3, 3, 4, 5]
Output: False
"""
def check_unique(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    if unique_lst == lst:
        return True
    else : 
        return False
if __name__ == "__main__":
    sample_input = [1,2,3,4,4,5]
    print("Output : ",check_unique(sample_input))