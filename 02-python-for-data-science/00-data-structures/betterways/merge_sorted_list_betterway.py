# this method preserves the duplicate entries the other file removes the duplicate because of set
def merge_two_sorted_lists(list1, list2):
    i , j = 0,0
    res = []
    while i<len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    while i<len(list1):
        res.append(list1[i])
        i += 1
    while j<len(list2):
        res.append(list2[j])
        j += 1
    return res
if __name__ == "__main__":
    sample_input1 = [1,2,3,4,5]
    sample_input2 = [4,5,6,7,8]
    print("Output : ",merge_two_sorted_lists(sample_input1,sample_input2))