class RingBuffer:
    def __init__(self, capacity):
       self.capacity = capacity
       self.storage = []
       self.index = 0

    def append(self, item):
        # if the current length is less than the max length
        if len(self.storage) < self.capacity:
            # insert the item at the end of the list
            self.storage.insert(len(self.storage), item)
        # if it is currently at max length
        else:
            # replace whatever is at the current index with the item
            self.storage[self.index] = item

        # keep track of index -- if it's not at the end, add one to it
        if self.index < self.capacity - 1:
            self.index += 1
        # if it is at the end of the list, set it back to 0
        else:
            self.index = 0 

    def get(self):
        return self.storage