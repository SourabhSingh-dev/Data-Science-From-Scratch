"""
Rotate a List
Rotate a List (Without Slicing)

You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions without using slicing. A rotation shifts elements from the end of the list to the front.

Link : https://www.udemy.com/course/complete-machine-learning-nlp-bootcamp-mlops-deployment/learn/quiz/6596159#overview

Parameters:

lst (List of integers): The list to be rotated.

k (Integer): The number of positions to rotate the list.

Returns:

A list of integers rotated by k positions.

Example:

Input: lst = [1, 2, 3, 4, 5], k = 2
Output: [4, 5, 1, 2, 3]

Input: lst = [10, 20, 30, 40, 50], k = 3
Output: [30, 40, 50, 10, 20]
"""
def rotate_list(lst, k):
    length = len(lst)
    if (length == 0):
        return lst
    if k>length:
        k = k - ((k//length) * length)
    rotated_list = lst.copy()
    for i in range(0,length):
        new_index = i + k
        if (new_index>length-1):
            new_index -= length
        rotated_list[new_index] = lst[i]        
    return rotated_list
if __name__ == "__main__":
    sample_input = [10, 20, 30, 40, 50]
    k = 6
    print("Output : ",rotate_list(sample_input,k))