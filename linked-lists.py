
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


    def partition(self, x):
        """Partition a linked list around x."""

        current = self.tail = self.head
        
        while current:
            next_node = current.next
            current.next = None
            
            if current.data < x:
                current.next = self.head
                self.head = current
            else:
                self.tail.next = current
                self.tail = current
            
            current = next_node

        if self.tail.next is not None:
            self.tail.next = None


    def is_palindrome(self):
        """Check if a linked list is a palindrome."""

        length = self.get_length()
        stack = [self.head.data]
        current = self.head.next

        if length % 2 == 0:
            while current:
                if stack[-1] == current.data:
                    stack.pop()
                else:
                    stack.append(current.data)
                current = current.next
        
        else:
            middle_node = length // 2
            node_count = 1
            while current:
                if node_count == middle_node:
                    current = current.next
                else:
                    if stack[-1] == current.data:
                        stack.pop()
                    else:
                        stack.append(current.data)
                    current = current.next
                node_count += 1

        return False if stack else True


def delete_middle_node(node):
    node.data = node.next.data
    node.next = node.next.next


def sum_lists(list1, list2):
    return sum_one_list(list1) + sum_one_list(list2)

def sum_one_list(lst):
    mult = 1
    list_sum = 0

    current = lst.head

    while current:
        list_sum += (current.data * mult)
        mult *= 10
        current = current.next

    return list_sum


def get_interesecting(linklist1, linklist2):
    """Determine if two lists intersect and return the intersecting node."""

    if linklist1.tail is not linklist2.tail:
        return None

    len_list1 = linklist1.get_length()
    len_list2 = linklist2.get_length()

    if len_list1 != len_list2:
        difference = len_list1 - len_list2
        if difference < 0:
            move_head(linklist2, difference)
        else:
            move_head(linklist1, difference)
            
    return find_intersecting_node(linklist1, linklist2)


def find_intersecting_node(list1, list2):
    current1 = list1.head
    current2 = list2.head

    while current1 is not current2:
        current1 = current1.next
        current2 = current2.next

    return current1


def move_head(lst, difference):
    current = lst.head
    for i in range(difference):
        lst.head = current.next
        current = current.next


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
print("Kth to Last Node -> e")
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

# Testing sum lists
seven = Node(7)
one = Node(1)
six = Node(6)
five = Node(5)
nine = Node(9)
two = Node(2)
ll_1 = LinkedList(seven)
ll_2 = LinkedList(five)
seven.next = one
one.next = six
five.next = nine
nine.next = two
print("Sum Lists -> 912")
print(sum_lists(ll_1, ll_2))

# Testing palindrome
b1 = Node("b")
i = Node("i")
b2 = Node("b")
ll_bib = LinkedList(b1)
b1.next = i
i.next = b2
r = Node("r")
o = Node("o")
c = Node("c")
k = Node("k")
ll_rock = LinkedList(r)
r.next = o
o.next = c
c.next = k
print("Test if bib is a palindrome -> True")
print(ll_bib.is_palindrome())
print("Test if rock is a palindrome -> False")
print(ll_rock.is_palindrome())

# Testing intersection
h = Node("h")
e = Node("e")
l1 = Node("l")
l2 = Node("l")
o = Node("o")
w = Node("w")
h.next = e
e.next = l1
l1.next = l2
l2.next = o
w.next = o
ll1 = LinkedList(h, o)
ll2 = LinkedList(w, o)
print("Test intersection hello, wo -> Node o")
print(get_interesecting(ll1, ll2))
print("test intersection rock, bib -> None")
print(get_interesecting(ll_rock, ll_bib))

