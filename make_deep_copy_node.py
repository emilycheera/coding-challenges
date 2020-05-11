class Node(object):
    """Node class."""

    def __init__(self, value, children):
        self.value = value
        self.children = children

"""Write a function that takes in a node and its children
and returns a new node that is a duplicate of that node"""


def create_node_copy(node):
  
  new_node = Node(node.value, [])
  
  for child in node.children:
    if isinstance(child, Node):
      new_node.children.append(create_node_copy(child))
    else:
      new_node.children.append(child)
  
  return new_node
  

def deep_print(node):
  
  print(node.value)
  
  for child in node.children:
    if isinstance(child, Node):
      deep_print(child)
    else:
      print(child)