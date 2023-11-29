class MaxHeap:

    def __init__(self, size=0):
        self.heap = [None] * size
        self.size = size

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
                    print("Item already exists in the heap")
                    return False
                else:
                    item_index += 1
            self.heap[item_index] = item
            self._bubble_up(item_index + 1)
            return True

    def _bubble_up(self, child_index):
        parent_index = child_index // 2
        if child_index > 1 and self.heap[child_index - 1] > self.heap[parent_index - 1]:
            self.heap[child_index - 1], self.heap[parent_index - 1] = self.heap[parent_index - 1], self.heap[child_index - 1]
            self._bubble_up(parent_index)

    def peek(self):  # Leo
        '''returns max without changing the heap, returns None if the heap
        is empty'''
        if self.is_empty():
            return None
        else:
            return self.heap[0]

    def dequeue(self):  # Leo
        '''returns max and removes it from the heap and restores the heap
        property
        returns None if the heap is empty'''
        if self.is_empty():
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
            self._bubble_down(1)
            del(self.heap[-1])
            return max

    def _bubble_down(self, parent_index):
        left_child = 2 * parent_index
        right_child = 2 * parent_index + 1
        if left_child - 1 < len(self.heap) and self.heap[left_child - 1] is not None:
            if self.heap[right_child - 1] is not None and self.heap[right_child - 1] > self.heap[left_child - 1]:
                if self.heap[parent_index - 1] < self.heap[right_child - 1]:
                    self.heap[parent_index - 1], self.heap[right_child - 1] = self.heap[right_child - 1], self.heap[parent_index - 1]
                    self._bubble_down(right_child)
            else:
                if self.heap[left_child - 1] > self.heap[parent_index - 1]:
                    self.heap[parent_index - 1], self.heap[left_child - 1] = self.heap[left_child - 1], self.heap[parent_index - 1]
                    self._bubble_down(left_child)

    def contents(self):  # Casey
        '''returns a list of contents of the heap in the order it is
        stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        return self.heap

    # def build_heap(self, alist):  # Chris
    #     '''Discards all items in the current heap and builds a heap from
    #     the items in alist using the bottom-up construction method.
    #     If the capacity of the current heap is less than the number of
    #     items in alist, the capacity of the heap will be increased to
    #     accommodate the items in alist'''
    #     self.heap = [None]*self.size
        # sortedAList = self.selectionSort(alist)
        # sortedAList.reverse()
        # if len(sortedAList) > self.get_capacity():
        #     self.heap = [None] * len(sortedAList)
        # for x in sortedAList:
        #     self.enqueue(x)

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from
        the items in alist using the bottom-up construction method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to
        accommodate the items in alist'''
        self.heap = [None] * self.size
        # Perform bottom-up construction starting from the last non-leaf node
        for i in range(self._parent_index(len(alist) - 1), -1, -1):
            self._heapify_down_from_index(i)

    def _heapify_down_from_index(self, index):
        while self._has_left_child(index):
            larger_child_index = self._get_larger_child_index(index)

            if self.heap[index] > self.heap[larger_child_index]:
                break
            else:
                self._swap(index, larger_child_index)

            index = larger_child_index

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

    def is_empty(self):  # Chris
        '''returns True if the heap is empty, false otherwise'''
        return self.heap[0] is None

    def is_full(self):  # Leo
        '''returns True if the heap is full, false otherwise'''
        return None not in self.heap

    def get_capacity(self):  # Casey
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold
        the heap can hold'''
        return len(self.heap)

    def get_size(self):  # Casey
        '''the actual number of elements in the heap, not the capacity'''
        heap_len = 0
        for el in self.heap:
            if el is not None:
                heap_len += 1
            else:
                heap_len += 0
        return heap_len

    def perc_down(self, i):  # Chris
        '''where the parameter i is an index in the heap and perc_down
        moves the element stored
        at that location to its proper place in the heap rearranging
        elements as it goes.'''
        item = self.heap[i]
        small_index = 0
        while i < int(self.size / 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if right < self.size and self.heap[left] < self.heap[right]:
                small_index = right
            else:
                small_index = left
            if item >= self.heap[small_index]:
                break
            self.heap[pos] = self.heap[small_index]
            i = small_index
        self.heap[small_index] = item

    def perc_up(self, i):  # Chris
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

    def heap_sort_ascending(self, alist):  # Casey
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a
        new heap using
        the items in alist, then mutate alist to put the items in
        ascending order'''
        new_heap = self.build_heap(alist)
        ascending_list = self.selectionSort(new_heap)

        return ascending_list