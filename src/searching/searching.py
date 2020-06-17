# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here    
    if len(arr) == 0:
        return -1
    if len(arr) == 1 and arr[0] == target:
        return start
    if start == end and start != target:
        return -1

    # set up new search arr
    # search_arr = arr[start:end]
    # Select midpoint and compare midpoint to target
    midpoint = (end + start) // 2
    if arr[midpoint] == target:
        return midpoint
    # If midpoint is not target, perform recursion call using midpoint as new endpoint
    elif arr[midpoint] > target:
        return binary_search(arr, target, start, midpoint )
    else:
        return binary_search(arr, target, midpoint + 1, end)

    pass



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    if arr[0] < arr[len(arr)-1]:
        return binary_search(arr, target, 0, len(arr) - 1)
    else:
        transform = [i * -1 for i in arr]        
        return binary_search(transform, target * -1, 0, len(transform) - 1)