"""
Reverse a List
Reverse a List (Non-Slicing Approach)

You are given a list of integers. Write a Python program that reverses the list without using slicing (lst[::-1]). The program should return the reversed list.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596149#overview

Parameters:

lst (List of integers): The list of integers to be reversed.

Returns:

A list of integers where the order of elements is reversed from the input list.

Example:

Input: lst = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""
def reverse_list(lst):
    rvs_lst = []
    for i in range(len(lst)-1,-1,-1):
        rvs_lst.append(lst[i])
    return rvs_lst  
input_list = input("Enter the numbers separated by space : ")
lst = input_list.split()
print(reverse_list(lst))
