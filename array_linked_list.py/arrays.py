

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.elements = [None]*capacity



# Double the size of the given array
def resize_array(array):
    new_capacity = array.capacity * 2 
    new_elements = [None] * new_capacity
    for i in range(array.count):
        new_elements[i] = array.elements[i]
    array.capacity = new_capacity
    array.elements = new_elements


# Return an element of a given array at a given index
# Throw an error if array is out of the current count
def array_read(array, index):
    if index >= array.count:
        print(f'Error, element {index} is out of range.')
    
    return array.elements[index]
    


# Insert an element in a given array at a given index
# Throw an error if array is out of the current count
# Resize the array if the number of elements is over capacity
# Move the elements to create a space at 'index'
# Think about where to start!
# Add the new element to the array and update the count
def array_insert(array, element, index):
    if index >= array.capacity:
        print(f'Error, array is too small increase size')
    if array.count == array.capacity:
        resize_array(array)
    for i in range(array.count, index, -1):
        array.elements[i] = array.elements[i-1]
    array.elements[index] = element
    array.count += 1



# Add an element to the end of the given array
# Hint, this can be done with one line of code
# (Without using a built in function)
def array_append(array):
    array_insert(array, array.element, array.count)
    
# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove(array, element):
    removed = False
    current = 0
    while not removed:
        if current >= array.count:
            print('Error, element is not found')
            break
        if array.elements[current] == element:
            removed = True
            for i in range(current, array.count):
                array.elements[i] = array.elements[i+1]
            
            array.count -= 1
        else:
            current += 1

    


# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
# Throw an error if array is out of the current count
def array_pop(array, index):
    if index >= array.count or index < 0:
        print(f'Error, element {index} is out of range')
        return None
    return_val = array.elements[index]
    for i in range(index + 1, array.count):
        array.elements[i - 1] = array.elements[i]

    array.count -= 1
    array.elements[array.count] = None

    return return_val


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.count):
        string += str(array.elements[i])
        if i < array.count - 1:
            string += ", "

    string += "]"
    print(string)


# # Testing
# arr = array(1)

# array_insert(arr, "STRING1", 0)
# array_print(arr)
# array_pop(arr, 0)
# array_print(arr)
# array_insert(arr, "STRING1", 0)
# array_append(arr, "STRING4")
# array_insert(arr, "STRING2", 1)
# array_insert(arr, "STRING3", 2)
# array_print(arr)
