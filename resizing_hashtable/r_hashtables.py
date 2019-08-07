

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity
        self.count = 0

# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for i in string:
        hash = ((hash << 5)+ hash) + ord(i)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    # getting the hashed key and location of the Node
    index = hash(key, hash_table.capacity)
    # bring current value in a variable
    current = hash_table.storage[index]
    # create a new link_pair
    
    while current is not None and current.key != key:
        current = current.next
    if current is None:
        new_pair = LinkedPair(key, value)
        head = current
        current = new_pair
        new_pair.next = head

        if new_pair.next is None:
            hash_table.count += 1
    


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    linked_pair = LinkedPair(key, value)
    if hash_table.storage[index].key != key:
        print(f'Error, key {key} cannot be found')
    if hash_table.storage[index].key is not None and len(hash_table.storage[index]) == 1:
        if hash_table.storage[index].value == linked_pair.value:
            hash_table.storage[index] = None
        




# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    cur = hash_table.storage[index]
    if cur is None:
        return None
    while cur is not None and cur.key != key:
        cur = cur.next
    
    return cur.value
    
    


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_hash_table = HashTable(hash_table.capacity * 2)
    for i in range(hash_table.count):
        current = hash_table.storage[i]
        while current is not None:
            hash_table_insert(new_hash_table, current.key, current.value)
            current = current.next
    return new_hash_table

    

def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
