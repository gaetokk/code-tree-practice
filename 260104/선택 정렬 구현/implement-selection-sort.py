n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def select_sort(arr, n):
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        tmp = arr[i]
        arr[i] = arr[min]
        arr[min] = tmp
    return arr

for i in select_sort(arr, n):
    print(i, end=' ')
        