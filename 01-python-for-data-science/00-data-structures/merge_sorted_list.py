"""
Merge two sorted List
Merge Two Sorted Lists

You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted list. The resulting list should also be in non-decreasing order.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596157#overview

Parameters:

list1 (List of integers): The first sorted list.

list2 (List of integers): The second sorted list.

Returns:

A single list of integers, containing all elements from list1 and list2, sorted in non-decreasing order.

Example:

Input: list1 = [1, 3, 5], list2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Input: list1 = [1, 4, 7], list2 = [2, 3, 5, 8]
Output: [1, 2, 3, 4, 5, 7, 8]
"""

def merge_two_sorted_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    merge_set = set1.union(set2)
    merge_list = list(merge_set)
    merge_list.sort()
    return merge_list

if __name__ == "__main__":
    sample_input1 = [1,2,3,4,5]
    sample_input2 = [4,5,6,7,8]
    print("Output : ",merge_two_sorted_lists(sample_input1,sample_input2))