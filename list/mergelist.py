
#合并两个顺序表

def merge_list(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    out_list = []
    i = 0
    j = 0
    while i<length1 and j<length2:
        a, b = list1[i], list2[j]
        if a<=b:
            c = a
            i += 1
        else:
            c = b
            j += 1

        out_list.append(c)

    if i<length1:
        for k in range(i, length1):
            out_list.append(list1[k])
    if j<length2:
        for k in range(j, length2):
            out_list.append(list2[k])
    return out_list


        
