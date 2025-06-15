def rotate_list(lst, k):
    if len(lst) == 0:
        return lst
    k = k%len(lst)
    for i in range(k):
        last_element = lst.pop()
        lst.insert(0,last_element)
    return lst
if __name__ == "__main__":
    sample_input = [10, 20, 30, 40, 50]
    k = 6
    print("Output : ",rotate_list(sample_input,k))