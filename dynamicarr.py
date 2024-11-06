import ctypes

class DynamicArray:
    def __init__(self):
        # Initialize with a capacity of 1 and no elements
        self._size = 0
        self._capacity = 1
        self._array = self._create_array(self._capacity)

    def __len__(self):
        # Return the number of elements in the array
        return self._size

    def __repr__(self):
        # Return a readable string representation of the array contents
        return f"DynamicArray({[self.get_item(i) for i in range(self._size)]})"

    def append(self, item):
        # Add an item to the array, resizing if necessary
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = item
        self._size += 1

    def get_item(self, index):
        # Retrieve the item at a given index
        if not 0 <= index < self._size:
            raise IndexError("Index out of range.")
        return self._array[index]

    def remove_item(self, item):
        # Remove the first occurrence of an item, resizing if necessary
        for i in range(self._size):
            if self._array[i] == item:
                # Shift elements to fill the gap
                for j in range(i, self._size - 1):
                    self._array[j] = self._array[j + 1]
                self._size -= 1
                # Shrink capacity if necessary
                if self._size < self._capacity // 4:
                    self._resize(self._capacity // 2)
                return
        raise ValueError("Item not found in list.")

    def _create_array(self, capacity):
        # Create a new array with the given capacity
        return (ctypes.c_int * capacity)()

    def _resize(self, new_capacity):
        # Resize the internal storage to the new capacity
        if new_capacity < 1:
            new_capacity = 1
        new_array = self._create_array(new_capacity)
        # Copy items to the new array
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

# Usage example
if __name__ == "__main__":
    my_array = DynamicArray()
    my_array.append(10)
    my_array.append(20)
    my_array.append(30)
    my_array.append(40)
    my_array.append(50)

    print("Array length:", len(my_array))
    print("Contents of the array:", my_array)

    my_array.append(60)
    print("Array after appending 60:", my_array)
    print("Array length after appending:", len(my_array))
    print("Item at index 2:", my_array.get_item(2))

    my_array.remove_item(10)
    print("Array after removing 10:", my_array)
    print("Array length after removing:", len(my_array))