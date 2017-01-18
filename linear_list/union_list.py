#union list like set

def union_list(list1, list2):
    length1 = len(list1)
    length2 = len(list2)
    out_list = list2.copy()

    for i in range(length1):
        item = list1[i]
        for j in range(length2):
            if item == list2[j]:
                break
        else:
            out_list.append(item)
    return out_list
        
