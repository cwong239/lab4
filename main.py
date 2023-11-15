class MaxHeap:

    def __init__(self, capacity):
        self.heap = [None]*capacity
        
    def enqueue(self, item): #Leo
        '''inserts "item" into the heap, returns true if successful, false
        if there is no room in the heap
        "item" can be any primitive or ***object*** that can be compared
        with other items using the < operator'''
        if not self.is_full():
            for items in self.heap:
                if item == items:
                    return False
            self.heap.append(item)
            item_index = self.heap.index(item) + 1
            self._bubble_up(item_index)
        else:
            return False

    def _bubble_up(self, child_index):
        parent_index = child_index // 2
        if child_index > 0 and self.heap[child_index] > self.heap[parent_index]:
            self.heap[child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[child_index]
            self._bubble_up(child_index)
            
    def peek(self):  #Leo
        '''returns max without changing the heap, returns None if the heap
        is empty'''
        if self.is_empty():
            return None
        else:
            return self.heap[0]

    def dequeue(self): #Leo
        '''returns max and removes it from the heap and restores the heap
        property
        returns None if the heap is empty'''
        if self.is_empty():
            return None
        else:
            current_index = 0
            while self.heap[current_index + 1] is not None:
                current_index += 1
            max = self.heap[0]
            self.heap[0] = self.heap[current_index]
            self._bubble_down(1)
            return max

    def _bubble_down(self, parent_index):
        left_child = 2 * parent_index
        right_child = 2 * parent_index + 1
        if self.heap[parent_index] < self.heap[left_child]:
            self.heap[parent_index], self.heap[left_child] = self.heap[left_child], self.heap[parent_index]
            self._bubble_down(left_child)
        elif self.heap[parent_index] < self.heap[right_child]:
            self.heap[parent_index], self.heap[right_child] = self.heap[right_child], self.heap[parent_index]
            self._bubble_down(right_child)
            
    def contents(self): #Casey
        '''returns a list of contents of the heap in the order it is
        stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heap
        
    def build_heap(self, alist): #Chris
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method. 
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to 
        accommodate the items in alist'''
        self.heap.clear()
        sortedAList = self.selectionSort(alist)
        sortedAList.reverse()
        if len(sortedAList)>len(self.heap):
            self.heap = [None]*len(sortedAList)
        for x in sortedAList:
            self.enqueue(x)

    def selectionSort(self, my_list):
        for i, x in enumerate(my_list):
            smallest = x
            min_index = i
            for j in range(i + 1, len(my_list)):
                if smallest > my_list[j]:
                    smallest = my_list[j]
                    min_index = j
            my_list[i], my_list[min_index] = smallest, x
        return my_list

    def is_empty(self): #Chris
        '''returns True if the heap is empty, false otherwise'''
        return len(self.heap) == 0
        
    def is_full(self): #Leo
        '''returns True if the heap is full, false otherwise'''
        return None not in self.heap

    def get_capacity(self): #Casey
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold
        the heap can hold'''
        return len(self.heap)

    def get_size(self): #Casey
        '''the actual number of elements in the heap, not the capacity'''
        heap_len = 0
        for el in self.heap:
            if self.heap[el] is not None:
                heap_len += 1
            else:
                heap_len += 0
        return heap_len

    def perc_down(self, i): #Chris
        '''where the parameter i is an index in the heap and perc_down
        moves the element stored
        at that location to its proper place in the heap rearranging
        elements as it goes.'''
        item = self.heap[i]
        small_index = 0
        while i < int(self.length / 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if right < self.length and self.heap[left] < self.heap[right]:
                small_index = right
            else:
                small_index = left
            if item >= self.heap[small_index]:
                break
            self.heap[pos] = self.heap[small_index]
            i = small_index
        self.heap[small_index] = item

    def perc_up(self, i): #Chris
        '''where the parameter i is an index in the heap and perc_up moves
        the element stored
        at that location to its proper place in the heap rearranging
        elements as it goes.'''
        parentIndex = (i - 1) // 2
        value = self.heap[i]
        while i > 0 and value > self.heap[parentIndex]:
            self.heap[i] = self.heap[parentIndex]
            i = parentIndex
            parentIndex = (parentIndex - 1) // 2
        self.heap[i] = value
        self.length += 1

    def heap_sort_ascending(self, alist): #Casey
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a
        new heap using
        the items in alist, then mutate alist to put the items in
        ascending order'''
        new_heap = self.build_heap(alist)
        ascending_list = self.selectionSort(new_heap)

        return ascending_list
