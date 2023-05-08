def merge_asc(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result
lst1 = [1,2,3,4,5,6,7,8,9,10,19,24,12,6,129,59,1,2000,3,56]
lst2 = [20,21,22,23,24,25,26,27]
lst3 = [30,29,31,33,19,20,31,21,59]
print(sorted((lst1)))
print(sorted((lst2)))
print(sorted((lst3)))
