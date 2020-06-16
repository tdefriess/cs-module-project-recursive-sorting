# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # Base case
    if len(arr) == 0:
        return -1
    if len(arr) == 1 and arr[0] == target:
        return start

    # set up new search arr
    # search_arr = arr[start:end]
    # Select midpoint and compare midpoint to target
    midpoint = (end + start) // 2
    if arr[midpoint] == target:
        return midpoint
    # If midpoint is not target, perform recursion call using midpoint as new endpoint
    elif arr[midpoint] > target:
        return binary_search(arr, target, start, midpoint)
    else:
        return binary_search(arr, target, midpoint, end)

    pass



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here