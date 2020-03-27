
class SetOfStacks():
    """A set of stacks."""

    # new stack should be created when a stack reaches capacity
    # want the new stack to append to self.stacks

    def __init__(self, capacity, stacks=None):
        
        self.capacity = capacity
        self.stacks = stacks or [[]]

    def push(self, item):
        """Add item to top of stack."""

        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([item])
        else:
            self.stacks[-1].append(item)

    def pop(self):
        """Remove an item from the top of the stack."""

        if len(self.stacks) == 1 and not self.stacks[-1]:
            return None
        
        if len(self.stacks) > 1 and len(self.stacks[-1]) == 1:
            item = self.stacks[-1].pop()
            self.stacks.pop() # Remove empty list
            return item
        
        return self.stacks[-1].pop()

    def popAt(self, idx):
        """Remove an item at a specific index."""

        stacks_idx = (idx // self.capacity)
        within_stack_idx = (idx % self.capacity)

        return self.stacks[stacks_idx].pop(within_stack_idx)


# Testing set of stacks
sos = SetOfStacks(5, [[3, 4, 5, 6, 6], [4, 5, 3, 5]])
print("Test sos.push(8) -> sos should be [[3, 4, 5, 6, 6], [4, 5, 3, 5, 8]]")
sos.push(8)
print(sos.stacks)
print("Test sos.push(9) -> sos should be [[3, 4, 5, 6, 6], [4, 5, 3, 5, 8], [9]]")
sos.push(9)
print(sos.stacks)
print("Test sos.pop() -> sos should be [[3, 4, 5, 6, 6], [4, 5, 3, 5, 8]]")
sos.pop()
print(sos.stacks)
print("Test sos.popAt(3) -> 6")
print(sos.popAt(3))
print("Test sos.popAt(3) -> 6")
print(sos.popAt(3))









