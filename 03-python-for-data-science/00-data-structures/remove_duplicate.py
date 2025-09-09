"""
Remove Duplicate in a List
Remove Duplicates from a List

You are given a list of integers. Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements. The order of elements in the list should be maintained.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596145#overview

Parameters:

lst (List of integers): The list of integers from which duplicates should be removed.

Returns:

A list of integers where all duplicates have been removed, preserving the original order.

Example:

Input: lst = [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]

Input: lst = [4, 5, 5, 4, 6, 7]
Output: [4, 5, 6, 7]


Note :- Please don't use set or inbuilt functions. Try to use brute force logic.
"""
def remove_duplicates(lst):
    new_lst = []
    for element in lst:
        if element not in new_lst:
            new_lst.append(element)
    return new_lst 
if __name__ == "__main__":
    sample_input = [1, 2, 2, 3, 4, 4, 5]
    print("Output:", remove_duplicates(sample_input))