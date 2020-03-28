"""Given a sorted, increasing order array with unique integer elements,
write an algorithm to create a binary search tree with minimal height."""

class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def make_bst(lst):

    if not lst:
        return

    middle = len(lst) // 2
    root = Node(lst[middle])

    left_nodes = lst[:middle]
    right_nodes = lst[middle + 1:]

    root.left = make_bst(left_nodes)
    root.right = make_bst(right_nodes)

    return root


testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
print(make_bst(testArray))


