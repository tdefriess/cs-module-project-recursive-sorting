# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # index trackers for arrA and arrB
    a_idx, b_idx = 0, 0
    for i in range(len(merged_arr)):
        # if index reaches end of one arr, fill using remaining elements from the other
        if a_idx == len(arrA):
            merged_arr[i] = arrB[b_idx]
            b_idx += 1
        elif b_idx == len(arrB):
            merged_arr[i] = arrA[a_idx]
            a_idx += 1
        # compare current indexes of A, B and assign as needed
        elif arrA[a_idx] < arrB[b_idx]:
            merged_arr[i] = arrA[a_idx]
            a_idx += 1
        else:
            merged_arr[i] = arrB[b_idx]
            b_idx += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # check for base case--empty or single item list
    if len(arr) <= 1:
        return arr
    # partition into left/right
    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    return merge(merge_sort(left), merge_sort(right))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

