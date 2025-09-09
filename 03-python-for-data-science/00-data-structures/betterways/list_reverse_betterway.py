def reverse_list(lst):
    start = 0
    end = len(lst)-1
    
    while start<end:
        lst[start],lst[end] = lst[end],lst[start]
        start += 1
        end -= 1
    return lst    
input_list = input("Enter the numbers separated by space : ")
lst = input_list.split()
print(reverse_list(lst))