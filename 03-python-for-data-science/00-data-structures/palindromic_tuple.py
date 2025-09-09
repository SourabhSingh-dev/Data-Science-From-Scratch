"""
Palindromic Tuple
Check if Tuple is Palindromic

Design a Python function named is_palindromic_tuple to check if a tuple is palindromic, meaning it reads the same forwards and backwards.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596167#overview

Parameters:

tup (tuple): The input tuple that you need to check for palindromic property.

Returns:

True if the tuple is palindromic, False otherwise.

Example:

Input: (1, 2, 3, 2, 1)
Output: True

Input: ('a', 'b', 'c', 'b', 'a')
Output: True

Input: (1, 2, 3, 4, 5)
Output: False

Input: ('x', 'y', 'z', 'x')
Output: False

Input: ('a',)
Output: True
"""
def is_palindromic_tuple(tup):
    is_palindrome = (tup[: :] == tup[: : -1])
    return is_palindrome
if __name__ == "__main__":
    sample_input = ('x', 'y', 'z', 'x')
    print('Output : ',is_palindromic_tuple(sample_input))