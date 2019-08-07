

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
    last_node = None

    while current is not None and current.key != key:
        last_node = current
        current = last_node.next
    if current is not None:
        current.value = value
    else:
        new_pair = LinkedPair(key, value)
        new_pair.next = hash_table.storage[index]
        hash_table.storage[index] = new_pair


    

    
    


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    cur = hash_table.storage[index]
    last_node = hash_table.storage[index]

    if cur is not None:
        while cur is not None:
            if cur.key == key:
                if cur is hash_table.storage[index]:
                    if cur.next is not None:
                        hash_table.storage[index] = None
                        return None
                    else:
                        hash_table.storage[index] = hash_table.storage[index].next
                        return None
                else:
                    if cur is not None:
                        last_node = cur.next
                        return None
                    else:
                        last_node.next = None
                        return None
            last_node = cur
            cur = cur.next
    if cur is None:
        print(f'{key} not Found')
        return None



        
                




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
    for i in range(0, len(hash_table.storage)):
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
