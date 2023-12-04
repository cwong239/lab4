class MaxHeap:
    def __init__(self, size = 0):
        self.heap = [None] * size
        self.size = size

    
    def get_size(self):
        return self.size
    def contents(self):
        temp = []
        for x in self.heap:
            if x is not None:
                temp.append(x)
        return temp
    def get_capacity(self): #Casey
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold
        the heap can hold'''
        return len(self.heap)
    def is_full(self):  # Leo
        '''returns True if the heap is full, false otherwise'''
        return None not in self.heap
    def is_empty(self):  # Chris
        '''returns True if the heap is empty, false otherwise'''
        return self.heap[0] is None
    def enqueue(self, item):  # Leo
        '''inserts "item" into the heap, returns true if successful, false
        if there is no room in the heap
        "item" can be any primitive or ***object*** that can be compared
        with other items using the < operator'''
        if self.is_full():
            print("There is no room in the heap")
            return False
        else:
            item_index = 0
            while self.heap[item_index] is not None:
                if item == self.heap[item_index]:
                    
                    return False
                else:
                    item_index += 1
            self.heap[item_index] = item
            self.perc_up_enitre()
            return True
    
    def dequeue(self):  # Leo
        '''returns max and removes it from the heap and restores the heap
        property
        returns None if the heap is empty'''
        if self.heap == None:
            return None
        else:
            # Make the rightmost item on the list the top
            current_index = 0
            while current_index < self.get_size() - 1 and self.heap[current_index] is not None:
                current_index += 1
            max = self.heap[0]
            self.heap[0] = self.heap[current_index]
            self.heap[current_index] = None

            # Starting from the top, compare it to its children and recursively swap down
            self.perc_down_entire()
            
            self.heap.pop(self.size - 1)
           
            self.size = self.size - 1
            # del(self.heap[-1])
            
            return max
    def extract_max(self):
        if not self.heap:
            return None

        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self.perc_down()

        return max_value

    def build_heap(self, alist):
        
        
        self.heap = alist[:]
        # Perform bottom-up construction starting from the last non-leaf node
        for i in range(self._parent_index(len(self.heap) - 1), -1, -1):
            self.perc_down(i)
        
        if self.size == 0:
     
            self.size = len(self.heap)
        else:
           
            if self.size>len(self.heap):

                while not len(self.heap) == self.size:
                    self.heap.append(None)
            else:
                self.size = len(self.heap)

    def perc_up(self, i):
        while self._has_left_child(i):
            smaller_child_index = self._get_smaller_child_index(i)
            
            if self.heap[i] < self.heap[smaller_child_index]:
                break
            else:
                self._swap(i, smaller_child_index)

            i = smaller_child_index

    def perc_up_enitre(self):
        index = len(self.heap) - 1
        while self._has_parent(index) and self.heap[index] > self._parent(index):
            self._swap(index, self._parent_index(index))
            index = self._parent_index(index)

    def perc_down_entire(self):
        index = 0
        while self._has_left_child(index):
            if self._has_right_child(index):
                if self._right_child(index) > self._left_child_index(index):
                    self.heap[index], self.heap[2 * index + 2] = self.heap[2 * index + 2], self.heap[index]
            larger_child_index = self._get_larger_child_index(index)
            if self.heap[larger_child_index] is None:
                self.heap.remove(larger_child_index)
                larger_child_index = self._get_larger_child_index(index)
            if self.heap[index] > self.heap[larger_child_index]:
                break
            else:
                self._swap(index, larger_child_index)

            index = larger_child_index

    def perc_down(self, index):
        while self._has_left_child(index):
            larger_child_index = self._get_larger_child_index(index)
            
            if self.heap[index] > self.heap[larger_child_index]:
                break
            else:
                self._swap(index, larger_child_index)

            index = larger_child_index

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

    def heap_sort_ascending(self, alist): #Casey
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a
        new heap using
        the items in alist, then mutate alist to put the items in
        ascending order'''
        self.heap = []
        self.build_heap(alist)
        new_heap = self.contents()
        alist[:] = self.selectionSort(new_heap)

        return alist


    # Helper Methods
    def _get_larger_child_index(self, index):
        if not self._has_right_child(index):
            return self._left_child_index(index)
        else:
            if self.heap[self._left_child_index(index)] > self.heap[self._right_child_index(index)]:
                return self._left_child_index(index)
            else:
                return self._right_child_index(index)
            
    def _get_smaller_child_index(self, index):
        if not self._has_right_child(index):
            return self._left_child_index(index)
        else:
            if self.heap[self._left_child_index(index)] < self.heap[self._right_child_index(index)]:
                return self._left_child_index(index)
            else:
                return self._right_child_index(index)

    def _has_parent(self, index):
        return index > 0

    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)

    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)

    def _parent(self, index):
        return self.heap[self._parent_index(index)]

    def _left_child(self, index):
        return self.heap[self._left_child_index(index)]

    def _right_child(self, index):
        return self.heap[self._right_child_index(index)]

    def _parent_index(self, index):
        return (index - 1) // 2

    def _left_child_index(self, index):
        return 2 * index + 1

    def _right_child_index(self, index):
        return 2 * index + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
