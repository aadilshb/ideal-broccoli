import heapq
def kth_largest1(arr, k):
    arr1=arr.copy()
    for i in range(k-1):
        arr1.remove(max(arr1))
    return max(arr1)

def kth_largest2(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

def kth_largest3(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k - 1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

arr=[4,2,9,7,5,6,7,1,3]
k=4
print(kth_largest1(arr,k))
print(kth_largest2(arr,k))
print(kth_largest3(arr,k))