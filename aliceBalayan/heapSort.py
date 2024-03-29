'''
Heap Sort Algorithm 

It is used when you want to maintain particular ordering (min/max). 
Efficient in priority queues. 

Time complexity: O(n log(n)) faster than Quick Sort.

In this example, I will do min heap sort. 

'''
def heapify(vals, size, root):
    largest = root # assign root to be the largest value
    left_child = (2 * root) + 1 
    right_child = (2 * root) + 2
    
    # check numbers on the left side (child)
    if left_child < size and vals[left_child] > vals[largest]:
        largest = left_child

    # check numbers on the left side (child)
    if right_child < size and vals[right_child] > vals[largest]:
        largest = right_child

    # if needed, change the root with the largest number
    if largest != root:
        vals[root], vals[largest] = vals[largest], vals[root]
        # Heapify the root
        heapify(vals, size, largest)

# main function to sort array
def heap_sort(vals):
    n = len(vals)

    for i in range(n, -1, -1):
        heapify(vals, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        vals[i], vals[0] = vals[0], vals[i]
        heapify(vals, i, 0)

# display the result 
random_list_of_vals = [35, 12, 43, 8, 51]
heap_sort(random_list_of_vals)
print(random_list_of_vals)  
