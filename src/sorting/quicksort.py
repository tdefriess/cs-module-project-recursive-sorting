# What kind of imput?
# A list
def quicksort(data):
    # check if data has 1 or 0 elements
    # (base case) a side only contains a single element
    if len(data) <= 1:
        return data

    # Partition the Data
    # Start by choosing a pivot
    pivot = data[0]
    # Need to create storage for the LHS and the RHS
    left = []
    right = []

    # Need to loop through each item
    for current in data[1:]:
        # if its smaller or equal, add to LHS storage
        if current <= pivot:
            left.append(current)        
        # if its bigger, add to RHS storage
        else:
            right.append(current)

    # (recursive case) Recursively quick sort LHS and RHS
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([2,5,7,1,3,4,6,9,8]))