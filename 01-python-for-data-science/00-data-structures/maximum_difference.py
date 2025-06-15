"""
Maximum Difference between 2 consecutive elements in a List
Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach)

You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. The difference is defined as the absolute value of the difference between two consecutive elements.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596155#overview

Parameters:

lst (List of integers): A list of integers.

Returns:

An integer representing the maximum difference between two consecutive elements.

Example:

Input: lst = [1, 7, 3, 10, 5]
Output: 7

The maximum difference is between 3 and 10 (i.e., |3 - 10| = 7).

Input: lst = [10, 11, 15, 3]
Output: 12

The maximum difference is between 15 and 3 (i.e., |15 - 3| = 12).
"""
def max_consecutive_difference(lst):
    max_diff = 0
    for i in range(0,len(lst)-1):
        diff = lst[i] - lst[i+1]
        if (diff<0):
            diff *= -1
        if (max_diff<diff):
            max_diff = diff                
    return max_diff                         
if __name__ == "__main__":
    sample_input = [10,11,15,3]
    print("Output : ",max_consecutive_difference(sample_input))