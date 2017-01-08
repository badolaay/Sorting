def merge(P1, P2):
    i = 0
    j = 0
    result = []
    while i < len(P1) and j < len(P2):
        if P1[i] < P2[j]:
            result.append(P1[i])
            i += 1
        else:
            result.append(P2[j])
            j += 1
    if i < len(P1):
        result.extend(P1[i:])
    if j < len(P2):
        result.extend(P2[j:])
    return result


def merge_sort(A):
    x = len(A)
    if x == 1:
        return A
    mid = x // 2
    P1 = merge_sort(A[:mid])
    P2 = merge_sort(A[mid:])
    return merge(P1, P2)


A = merge_sort([3, 2, 1, 6, 5])
print("Sorted array is:")
print('\t'.join(map(str, A)))
