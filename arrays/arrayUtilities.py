class ArrayUtilities:
    def __init__(self, array=[], tam=0):
        self.array = array
        self.tam = tam

    def reverse_array(self):
        return self.array[::-1]

    # Rotate rotation_d positions: True-> counterclockwise, False-> clockwise
    def rotate_array(self, rotation_d=0, direction=True):
        previous_array = self.array
        if direction:
            self.rotate_lef(rotation_d)
        else:
            self.rotate_right(rotation_d)
        return previous_array

    def rotate_lef(self, rotation_d=0):
        temp = self.array[0]
        tam = len(self.array)
        rotation_d = rotation_d % tam
        if rotation_d != 0:
            pos = 0
            element_to_replace = self.array[pos]
            for i in range(0, len(self.array)):
                new_pos = pos - rotation_d
                if new_pos < 0:
                    new_pos = tam + new_pos
                temp = self.array[new_pos]
                self.array[new_pos] = element_to_replace
                element_to_replace = temp
                pos = new_pos

    def rotate_right(self, rotation_d=0):
        temp = self.array[0]
        tam = len(self.array)
        rotation_d = rotation_d % tam
        if rotation_d != 0:
            pos = 0
            element_to_replace = self.array[pos]
            for i in range(0, len(self.array)):
                new_pos = pos + rotation_d
                if new_pos >= tam:
                    new_pos = new_pos - tam
                temp = self.array[new_pos]
                self.array[new_pos] = element_to_replace
                element_to_replace = temp
                pos = new_pos

    # Sort the array, Incremental mode-> True, Decremental mode ->False
    def init_quick_sort(self, mode=True):
        previous_array = self.array
        if mode:
            self.quick_sort_in(0, len(self.array) - 1)
        else:
            self.quick_sort_de(0, len(self.array) - 1)
        return previous_array

    def quick_sort_in(self, l=0, r=0):
        if l >= r:
            return
        pivot = self.array[r]
        cnt = l
        for i in range(l, r + 1):
            if self.array[i] <= pivot:
                temp = self.array[cnt]
                self.array[cnt] = self.array[i]
                self.array[i] = temp
                cnt = cnt + 1
        self.quick_sort_in(l, cnt - 2)
        self.quick_sort_in(cnt, r)

    def quick_sort_de(self, l=0, r=0):
        if l >= r:
            return
        pivot = self.array[r]
        cnt = l
        for i in range(l, r + 1):
            if self.array[i] >= pivot:
                temp = self.array[cnt]
                self.array[cnt] = self.array[i]
                self.array[i] = temp
                cnt = cnt + 1
        self.quick_sort_de(l, cnt - 2)
        self.quick_sort_de(cnt, r)

    def search_max(self):
        max_element = self.array[0]
        for element in self.array:
            if max_element < element:
                max_element = element
        return max_element

    def search_min(self):
        min_element = self.array[0]
        for element in self.array:
            if min_element > element:
                min_element = element
        return min_element

    def init_binary_search(self, element=0):
        return self.binary_search(0, len(self.array) - 1, element)

    def binary_search(self, l=0, r=0, element=0):
        middle =int((r + l) / 2)
        pivot = self.array[middle]
        if pivot == element:
            return middle
        if r == l:
            return -1
        if pivot > element:
            return self.binary_search(l, middle, element)
        else:
            return self.binary_search(middle+1, r, element)

    def straight_forward_search(self, element = 0):
        for item in range(0,len(self.array)):
            if self.array[item] == element:
                return item
        return -1
