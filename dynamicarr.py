import ctypes

class DynamicList:
    def __init__(self):
        # Start with a small array capacity of 1 and no items
        self._count = 0
        self._storage = self._new_array(1)

    def __len__(self):
        # Number of items currently in the list
        return self._count

    def __repr__(self):
        # Return a readable version of the list contents
        return f"DynamicList({[self.get_item(i) for i in range(self._count)]})"

    def append(self, item):
        # Add a new item to the list, expanding capacity if needed
        if self._count == len(self._storage):
            self._resize(2 * len(self._storage))
        self._storage[self._count] = item
        self._count += 1

    def get_item(self, index):
        # Fetch an item at a specific index
        if not 0 <= index < self._count:
            raise IndexError("Index is out of range.")
        return self._storage[index]

    def remove_item(self, item):
        # Remove the first occurrence of an item from the list
        for i in range(self._count):
            if self._storage[i] == item:
                for j in range(i, self._count - 1):
                    self._storage[j] = self._storage[j + 1]
                self._count -= 1
                return
        raise ValueError("Item not found in list.")

    def _new_array(self, capacity):
        # Create a new array with the specified capacity
        return (ctypes.c_int * capacity)()

    def _resize(self, new_capacity):
        # Resize the internal storage to a new capacity
        new_storage = self._new_array(new_capacity)
        for i in range(self._count):
            new_storage[i] = self._storage[i]
        self._storage = new_storage

# Usage example
if __name__ == "__main__":
    my_list = DynamicList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    my_list.append(50)

    print("List length:", len(my_list))
    print("Contents of the list:", my_list)

    my_list.append(60)
    print("List after appending 60:", my_list)
    print("List length after appending:", len(my_list))
    print("Item at index 2:", my_list.get_item(2))

    my_list.remove_item(10)
    print("List after removing 10:", my_list)
    print("List length after removing:", len(my_list))