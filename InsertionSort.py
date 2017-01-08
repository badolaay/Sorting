def insertion_sort(A):
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


A = [2, 4, 1, 6, 5]
A = insertion_sort([2, 4, 1, 6, 5])
print("Sorted array is:")
print('\t'.join(map(str, A)))
