def check_list_equal(lst):
    first_item = lst[0]
    for item in lst:
        if item != first_item:
            return False
    return True

def merge_list(lst1, lst2):
    merged = list()
    for i in range(len(lst1)):
        merged.append(lst1[i] + lst2[i])
    return merged

def odd_candy(lst):
    output = list()
    for item in lst:
        if item % 2 == 1:
            item = item + 1
        output.append(item)
    return output

def adjust_algorithm(lst):
    print("Original:\t", lst)
    print()
    count = 0
    while not check_list_equal(lst):
        half_lst = [0] * len(lst)
        for i in range(len(lst)):
            if i == len(lst) - 1:
                half_lst[0] = lst[i] / 2
            else:
                half_lst[i + 1] = lst[i] / 2
            lst[i] -= lst[i] / 2
        print("Apply half:\t", lst)
        print("Candies gain:\t", half_lst)
        merged = merge_list(lst, half_lst)
        print("Apply merge:\t", merged)
        lst = odd_candy(merged)
        print("Apply odd:\t", lst)
        count += 1
        print()
    print("total iteration:\t", count)

adjust_algorithm([2, 100, 28, 4, 8, 10])
