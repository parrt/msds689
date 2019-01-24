from lolviz import *

class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = Tree(10)
mary = Tree(3)
april = Tree(13)
jim = Tree(2)
sri = Tree(21)
mike = Tree(7)

root.left = mary
root.right = april
mary.left = jim
mary.right = mike
april.right = sri

treeviz(root).view()
