

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None]*capacity

# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for i in string:
        hash = ((hash << 5) + hash) + ord(i)
    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    #getting the hash key
    key_hash = hash(key, hash_table.capacity)
    # create a new pair using the key and value passed in the fn
    new_pair = Pair(key, value)
    #getting index 
    index = key_hash % hash_table.capacity
    #if the index has pair, check if the keys match 
    if hash_table.storage[index] is not None:
        if key == hash_table.storage[index].key:
            print(f'Error, {key} has an accident with {hash_table.storage[index].key}')
        else:
            hash_table.storage[index].value = value
    else:
        hash_table.storage[index] = new_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    #get hashed key
    key_hash = hash(key, hash_table.capacity)
    #get index
    index = key_hash % hash_table.capacity
    #see if there is a value
    if hash_table.storage[index] is not None:
        hash_table.storage[index] = None
    else:
        print(f'{key} not found in table')

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    #get the hash key
    key_hash = hash(key, hash_table.capacity)
    #getting index
    index = key_hash % hash_table.capacity
    #if index is not none
    if hash_table.storage[index] is not None:
        #if the key is the same of what we trying to find
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value
    return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
