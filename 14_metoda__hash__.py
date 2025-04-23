'''
The hash method in Python is used to define how objects of a class are hashed. Here are some key points about hash:

It is called when hash() is invoked on an object, or when an object is used in a hash-based collection like set or dictionary.

hash should return an integer representing the hash value of the object.

The hash value is used by hash-based collections to determine where to store the object in memory.

Objects that compare equal must have the same hash value. So hash should be consistent with equality (eq).

Hash values should be unique and uniform across different runs of the program, so they should not depend on mutable properties of the object.

If hash is not defined, the default hash is the object's id. This may cause unexpected behavior in hash collisions.

Overriding hash is necessary for hash-based collections to function properly with custom classes.

hash should be overridden alongside eq to maintain the contract that equal objects must hash equally.

Making hash depend on mutable properties can cause confusing behavior when objects change.

So in summary, hash generates a hash code for instances of a class that is used by hash-based data structures. It should be implemented consistently with equality and aim for uniform distribution of hash values.

__hash__ powinna zwrucić wartość całkowita

'''

help(hash)


class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __eq__(self, other):
        return isinstance(other, Doc) and self.string == other.string

    def __hash__(self):
        return hash(self.string)


doc1 = Doc('OOP')
doc2 = Doc('OOP')
doc3 = Doc('Python')

doc1, doc2, doc3

hash(doc1)
docs = {doc1, doc2}
docs = {doc1: 'a'}
