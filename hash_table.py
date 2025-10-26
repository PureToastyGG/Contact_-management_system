class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return self.name + ": " + self.number
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''


class Node: 
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.next = None
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    pass # Delete this line when implementing the class

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self,key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
    
    def insert(self, key, value): 
        temp = Contact(key, value)  
        index = self.hash_function(key)
        current = self.data[index] 

        #If there are no values currently at that position, insert the input
        if self.data[index] is None:
            self.data[index] = Node(temp.name, temp)
            return  

        while current: #Keep iterating until you reach an empty spot
            if current.key == key:
                current.value = temp
                return
            
            if current.next is None:
                break #stops at last node

            current = current.next

        current.next = Node(temp.name, temp)
    
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None
    
    def print_table(self):
        counter = 0
        for current in self.data:
            if current:
                print(f"Index {counter}: " + str(current.value), end="")
                while current.next:
                    print(f" - " + str(current.next.value), end="")
                    current = current.next
                print()
            else:
                 print(f"Index {counter}: None")
            counter += 1
        pass
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    pass # Delete this line when implementing the class

# Test your hash table implementation here.  
'''table = HashTable(10)
contact_1 = Contact("Riley", "123-456-7890")
print(contact_1) # Riley: 123-456-7890 '''

contact_1 = Contact("Riley", "123-456-7890")
node_1 = Node(contact_1.name, contact_1)
print(node_1.key) # Riley 
print(node_1.value) # Riley: 123-456-7890 
print(node_1.next) # None 

print()

table = HashTable(10)
table.print_table()

print()

# Add some values 
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
# Print the new table structure 
table.print_table()

print()

# Search for a value
contact = table.search("John") 
print("\nSearch result:", contact)  # Search result: John: 909-876-1234

print()

# Edge Case #1 - Hash Collisons (assuming these hash to the same index) 
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function 
table.print_table()

print()

# Edge Case #2 - Duplicate Keys 
table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()

print()

# Edge Case #3 - Searching for a value not in the table
print(table.search("Chris")) # None

'''
Why is a hash table the right structure for fast lookups?
The hash table is the right structure for fast lookups because you can find items directly by the key. This is done by putting the object
in the index that relates to the keys Unicode value. This allows for the search to know almost instantly where the item would be based on
the key, and if the item isn't in that index than it isn't in the hash table at all.

How did you handle collisions?
I could've probably handled collisions slightly better but what I did was I used the typical strategy of having each indexed value as a linked
list, so if two inserted objects would belong in the same index, they simply do stay in the same index just know they are iterated through if
there is more than one value at that index. I ran into a little bit of trouble when trying to effiecntly find ways to print the different linked
list items. I ended up having a nested loop which would typically be O(n2) but that is only on iterations where there is a value at that index
and only iterates through the while loop if there is also a value at current.next. So I believe the way it is set up is decreased down to O(n).

When might an engineer choose a hash table over a list or tree?
It would be best for an engineer to use a hash table over a list or a tree whenever they want to be able to find values by a specific key. The
example used in the lessons was looking to see if someone has an account based on a username or email given. An example of when you would use
this off the top of my head would be a patient system at a hospital where you want to be able to find medical information based soley on name
look up.

'''