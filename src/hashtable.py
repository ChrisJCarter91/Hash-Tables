# '''
# Linked List hash table key/value pair
# '''

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        #Find index 
        index = self._hash_mod(key)
        #check if key value pair already exists and if not, create linked pair
        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key, value)
        #If it exists
        else:
            existing = self.storage[index]
            #If key is the same, change the value to avoid duplicate
            if existing.key == key:
                existing.value = value
                return
            #If not the same, then as long as there's a next, check for duplicate
            while existing.next:
                if existing.next.key == key:
                    existing.next.value = value
                    return

                else:
                    existing = existing.next
            #if at the end of the list there's no matching key, create next to last node
            existing.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        
        index = self._hash_mod(key)
        current = self.storage[index]

        if self.storage[index].key == key:
            self.storage[index] = self.storage[index].next
            return

        #if not on first level, check on linked list
        while current.next:
            if current.next.key == key:
                #point to next node in linked list
                current.next = current.next.next
                return
            else:
                current = current.next

        print(f"Key not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        
        index = self._hash_mod(key)

        current = self.storage[index]

        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        
        storage = [None] * self.capacity * 2
        #copy storage
        first_storage = self.storage
        #point storage to the new array
        self.storage = storage
        #double the capacity
        self.capacity *= 2
        #fill array with first_storage
        for i in first_storage:
            current = i
            while current:
                self.insert(current.key, current.value)
                current = current.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
