# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    result = []
    a_index = 0
    b_index = 0
    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] < arrB[b_index]:
            result.append(arrA[a_index])
            a_index += 1
        else:
            result.append(arrB[b_index])
            b_index += 1

    if a_index == len(arrA): result.extend(arrB[b_index:])

    else:
        result.extend(arrA[a_index:])

    return result
    # Your code here


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(array):
    # Your code here
    if len(array)<=1:
        return array
    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    return merge(left,right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

