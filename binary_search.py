def binary_search(A:list, n):
    """
    Searches for element 'n' in Sorted list 'A'
    :param A:list
    :param n:searches element
    :return:bool
    """
    midl_N = len(A)//2


    if A[midl_N] == n:
        print(True)
    elif len(A) == 1:
        print(False)
    elif A[midl_N] < n:
        binary_search(A[midl_N:], n)
    elif A[midl_N] > n:
        binary_search(A[:midl_N], n)


A = [i for i in range(11)]
print(A)

binary_search(A, 125)
