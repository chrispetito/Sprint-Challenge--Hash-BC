#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # insert weights with index
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    # subtract weight from ht limit
    for i in range(length):
        value = hash_table_retrieve(ht, limit-weights[i])
        # if it isn't none...
        if value is not None:
            # return key, value in ascending order
            if i > value:
                return (i, value)
            else:
                return (value, i)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
