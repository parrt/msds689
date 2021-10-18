class MinHeap:
    """
    Heap condition is that the root is smaller than either child.
    For efficiency we can use the (i, 2i+1, 2i+2) to represent
    the tree structure without pointers. To get the parent pointer we use i//2.
    """
    def __init__(self):
        self.nodes = [None]*5 # make a small heap to start out
        self.n = 0

    def __str__(self):
        # return f"{h.nodes[0:self.n]}"
        return self.encode(0)

    def encode(self, i):
        if i>=self.n:
            return ""
        l = MinHeap.left(i)
        r = MinHeap.right(i)
        v = self.nodes[i]
        if l>=self.n: # no left node and so no kids
            return str(v)
        if r>=self.n or self.nodes[r] is None: # no right node
            return f'( {str(v)} {self.encode(l)} _ )'
        if self.nodes[l] is None:
            return f'( {str(v)} _ {self.encode(r)} )'
        return f'( {str(v)} {self.encode(l)} {self.encode(r)} )'

    @staticmethod
    def left(i): return 2*i+1

    @staticmethod
    def right(i): return 2*i+2

    @staticmethod
    def parent(i): return i//2

    def insert(self, x):
        """
        To insert, we add the element to the end, which makes it the last leaf
        and then bubble it up until we find the right position. To bubble up
        means to swap the minimum child with the subtree root and then recurse.
        """
        print("insert", x, "at", self.n)
        # Make sure there is room and then add new new leaf
        if self.n >= len(self.nodes): # full?
            self.nodes = self.nodes + [None]*len(self.nodes) # double in size
        self.nodes[self.n] = x
        self.n += 1
        self.bubbleUp(self.n-1)

    def deleteMin(self):
        """
        To delete, take last leaf and put into root and bubble down. drop n by 1. delete
        last leaf.
        """
        if self.n<=0:
            return None
        m = self.nodes[0]
        print("deleteMin",m)
        if self.n>1: # swap
            self.nodes[0] = self.nodes[self.n-1]
            self.nodes[self.n - 1] = None # don't have to but wack that value
        self.n -= 1
        self.bubbleDown(0)
        return m

    def sorted(self):
        "Get sorted list of values. Warning destructive!"
        return [self.deleteMin() for i in range(self.n)]

    def bubbleUp(self, i):
        """
        Compare nodes[i] to its parent; if parent is smaller than swap
        and recursively bubble up on the root.
        """
        print("bubbleUp",i)
        if self.nodes[i] < self.nodes[MinHeap.parent(i)]:
            self.nodes[i], self.nodes[MinHeap.parent(i)] = self.nodes[MinHeap.parent(i)], self.nodes[i]
            self.bubbleUp(MinHeap.parent(i))

    def bubbleDown(self, i):
        """
        Find min child. If nodes[i] bigger than min child, swap nodes[i] with it
        and recursively bubble down on that min child
        """
        l = MinHeap.left(i)
        r = MinHeap.right(i)
        # TODO what if right but not left node?
        if l>=self.n: # no left node and so no kids
            return
        if r>=self.n: # no right node
            m = l
        else:
            m = l if self.nodes[l] < self.nodes[r] else r
        if self.nodes[m] < self.nodes[i]:
            self.nodes[i], self.nodes[m] = self.nodes[m], self.nodes[i]
            self.bubbleDown(m)


# h = MinHeap()
# h.insert(1)
# print(h)
#
# h = MinHeap()
# for x in [3, 2, 1]:
#     h.insert(x)
# print(h)
#
# h = MinHeap()
# for x in [2, 3, 1]:
#     h.insert(x)
# print(h)
#
# h = MinHeap()
# for x in [1,2,3]:
#     h.insert(x)
# print(h)
#
# h = MinHeap()
# for x in [1,1]:
#     h.insert(x)
# print(h)
#
# h = MinHeap()
# for x in [1,-1]:
#     h.insert(x)
# print(h)

h = MinHeap()
for x in [3,2,1,5,6,4]:
    h.insert(x)
print(h)
print("sorted", h.sorted())
for i in range(6):
    print("del", h.deleteMin(),"->",h)


# h = MinHeap()
# for x in reversed(range(1,10)):
#     h.insert(x)
# print(h)
#
# for x in range(10):
#     print(h.deleteMin())
# print(h)
