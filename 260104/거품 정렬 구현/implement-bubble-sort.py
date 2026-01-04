n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def bubble_sort(arr, n):
    for i in range(n-1):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    
    return arr

for i in bubble_sort(arr, n):
    print(i, end=' ')
    