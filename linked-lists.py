
class LinkedList():

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


    def print_nodes(self):
        current = self.head

        while current:
            print(current)
            current = current.next


    def get_length(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count


    def remove_duplicates(self):
        """Remove duplicate nodes from a linked list."""
        
        current = self.head
        nodes_set = {current.data}

        while current:
            if current.next.data in nodes_set:
                current.next = current.next.next
            else:
                nodes_set.add(current.next.data)
            current = current.next


    def find_kth_to_last_node(self, k):
        length = self.get_length()

        if k > length:
            return None

        node_from_beg = length - k

        count = 0
        current = self.head

        while count < node_from_beg:
            count += 1
            current = current.next

        return current


    def find_kth_to_last_node_runner(self, k):
        current = runner = self.head
        for i in range(k):
            if runner is None:
                return None
            runner = runner.next

        while runner:
            current = current.next
            runner = runner.next

        return current


    def partition(self, partition):
        
        pass



def delete_middle_node(node):

    node.data = node.next.data
    node.next = node.next.next


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node {self.data}"



# Testing remove duplicates
a = Node("a")
b = Node("b")
c = Node("c")
aa = Node("a")
ll = LinkedList(a)
a.next = b
b.next = c
c.next = aa
print("Linked List Before Removing Dups:")
ll.print_nodes()
ll.remove_duplicates()
print("Linked List After Removing Dups:")
ll.print_nodes()

# Testing find kth to last node
d = Node("d")
e = Node("e")
f = Node("f")
c.next = d
d.next = e
e.next = f
print("Kth to Last Node:")
print(ll.find_kth_to_last_node_runner(2))

# Testing delete middle node
print("Linked List Before Deleting Middle Node (d):")
ll.print_nodes()
delete_middle_node(d)
print("Linked List After Deleting Middle Node (d):")
ll.print_nodes()

# Testing partition
three = Node(3)
five1 = Node(5)
eight = Node(8)
five2 = Node(5)
ten = Node(10)
two = Node(2)
one = Node(1)
three.next = five1
five1.next = eight
eight.next = five2
five2.next = ten
ten.next = two
two.next = one
num_ll = LinkedList(three, one)
print("Linked List Before Partition:")
num_ll.print_nodes()
print("Linked List After Partition:")
num_ll.partition(5)
num_ll.print_nodes()







