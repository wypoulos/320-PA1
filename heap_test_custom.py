import heap

if __name__ == "__main__":
    A = heap.shuffled_list(20, 0)
    print("Complete Tree size 20:")
    heap.printCompleteTree(A)
    heap.buildHeap(A)
    print("After Build Heap")
    heap.printCompleteTree(A)
    print("After heapExtractMin")
    heap.heapExtractMin(A)
    heap.printCompleteTree(A)
    print("After heapInsert")
    heap.heapInsert(A, 9)
    heap.printCompleteTree(A)