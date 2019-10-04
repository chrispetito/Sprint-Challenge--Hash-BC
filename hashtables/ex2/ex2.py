#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(length):
        hash_table_insert(hashtable, tickets[i], i)
    # subtract weight from ht limit
    for i in range(length):
        value = hash_table_retrieve(hashtable, length-tickets[i])
        # if it isn't none...
        if value is not None:
            # return key, value in ascending order
            if i > value:
                return (i, value)
            else:
                return (value, i)

    return route
