# DAAHandsOn_11

## Output

![OutputDAAHandsOn11](https://github.com/user-attachments/assets/42b28ce2-411a-44b7-aefb-28048261e79b)


# DynamicArray

A Python implementation of a dynamic array (similar to a C++ vector) that only uses C-style arrays for storage. This `DynamicArray` class supports dynamic resizing and shrinking based on the number of elements, ensuring efficient memory usage.

## Features

- **Dynamic Resizing**: The array doubles in capacity when it reaches full capacity upon appending a new item.
- **Dynamic Shrinking**: The array halves in capacity when elements are removed and the size falls below a quarter of the current capacity.
- **C-style Array**: Uses low-level C-style integer arrays for internal storage.
- **Int-only Storage**: Assumes all data is of integer type.
- **Basic Operations**: Supports appending items, retrieving items by index, and removing items by value.

## Requirements

This class uses the `ctypes` module, which is included in the Python Standard Library. No external libraries are required.

## Usage

### Initializing the Dynamic Array

```python
from dynamic_array import DynamicArray

# Initialize an empty DynamicArray
my_array = DynamicArray()
# Append items to the array
my_array.append(10)
my_array.append(20)
my_array.append(30)

# Get an item by its index
print(my_array.get_item(1))  # Output: 20
# Remove the first occurrence of an item
my_array.remove_item(10)
# Get the number of elements in the array
print(len(my_array))  # Output: 2 (after removing an element)
# Print the contents of the array
print(my_array)  # Output: DynamicArray([20, 30])
```
