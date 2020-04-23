# construct a max-heap.

arr = [ 1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

def heapify(arr, n, i):

    largest = i
    left_child = 2*i + 1
    right_child = 2*i + 2

    if left_child < n and arr[left_child] > arr[largest]:
       largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
       largest = right_child

    if largest != i:
       tmp = arr[i]
       arr[i] = arr[largest]
       arr[largest] = tmp
      
       heapify(arr, n, largest)






def build_heap(arr, n):
    last_non_leaf = int(n/2) -1 
    for i in range( last_non_leaf, -1, -1):
        heapify(arr, n, i)


build_heap(arr, len(arr))

print(arr[0])
