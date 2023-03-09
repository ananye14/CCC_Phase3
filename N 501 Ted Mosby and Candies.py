def binary_search(arr, x):
    # Returns True if x is present in the array arr, False otherwise
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

n = int(input())
a = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

# Sort the array A to perform binary search
a.sort()

for i in range(m):
    if binary_search(a, c[i]):
        print("Happy Halloween!")
    else:
        print("Tricky!")
