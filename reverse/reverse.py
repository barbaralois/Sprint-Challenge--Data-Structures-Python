class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if length is 0
        if self.head is None:
            return None
        # if length is 1
        if self.head.get_next() is None:
            return
        # otherwise, items need to be reversed
        else:
            # set variables
            current_node = node
            previous_node = prev
            next_node = node.get_next()

            # while not the last value or 2nd to last value
            while next_node.get_next() is not None:
                # current node's new next is the previous -- swaps it to the other side
                current_node.set_next(previous_node)
                # then set the previous node to the item that was after it
                previous_node = current_node
                # set the current node to the item that was after it
                current_node = next_node
                # set the next node to what comes after that new current (prior next value)
                next_node = current_node.get_next()
            
            # when at the 2nd to last item...
            current_node.set_next(previous_node)
            # set the new head/first item
            self.head = next_node
            # connect it to the current node (aka the item that previously came before it)
            self.head.set_next(current_node)
