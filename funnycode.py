class MaxHeap:
    def __init__(self, size = 0):
        self.heap = [None] * size
        self.size = size

    
    def get_size(self):
        return self.size
    def contents(self):
        return self.heap
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
            self.perc_up()
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
            self.perc_down()
            del(self.heap[-1])
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
            self.perc_down_fromIndex(i)
        if self.size>len(self.heap):

            while not len(self.heap) == self.size:
                self.heap.append(None)
        else:
            self.size = len(self.heap)

    def perc_up(self):
        index = len(self.heap) - 1
        while self._has_parent(index) and self.heap[index] > self._parent(index):
            self._swap(index, self._parent_index(index))
            index = self._parent_index(index)

    def perc_down(self):
        index = 0
        while self._has_left_child(index):
            larger_child_index = self._get_larger_child_index(index)
            
            if self.heap[index] > self.heap[larger_child_index]:
                break
            else:
                self._swap(index, larger_child_index)

            index = larger_child_index

    def perc_down_fromIndex(self, index):
        while self._has_left_child(index):
            larger_child_index = self._get_larger_child_index(index)

            if self.heap[index] > self.heap[larger_child_index]:
                break
            else:
                self._swap(index, larger_child_index)

            index = larger_child_index


    # Helper Methods
    def _get_larger_child_index(self, index):
        if not self._has_right_child(index):
            return self._left_child_index(index)
        else:
            if self.heap[self._left_child_index(index)] > self.heap[self._right_child_index(index)]:
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
    