from lolviz import *
import time
import os
import psutil

class TrieNode:
    def __init__(self):
        self.edges = {} # easier to debug


def add(p:TrieNode, s:str, i=0) -> None:
    if i>=len(s): return
    if s[i] not in p.edges:
        p.edges[s[i]] = TrieNode()
    add(p.edges[s[i]], s, i+1)


def create_trie(words):
    root = TrieNode()
    for w in words:
        w = w.strip().lower()
        if w.isalpha():
            add(root, w)
    return root


def search(root:TrieNode, s:str, i=0) -> TrieNode:
    "Return node reached by s"
    p = root
    while p is not None:
        if i>=len(s): return p
        if s[i] not in p.edges: return None
        p = p.edges[s[i]]
        i += 1
    return None


def suffixes(root:TrieNode, prefix:str):
    "Find all words with a given (possibly empty) prefix"
    start = search(root, prefix)
    paths = []
    if start is not None:
        suffixes_(start, path="", paths=paths)
    return paths


def suffixes_(p:TrieNode, path, paths):
    "no possibility of cycle"
    if len(p.edges)==0: # have we reached stop state?
        paths.append(path)
        return
    for c in p.edges:
        q = p.edges[c]
        suffixes_(q, path + c, paths)


if __name__ == '__main__':
    with open("/usr/share/dict/words") as f:  # linux likely /usr/dict/words
        words = f.readlines()
    words = words[:50_000] # reduce size of word list during development
    words = ['apple','ape','axe','box']
    print(f"{len(words)} words in dictionary")

    root = create_trie(words)
    objviz(root).view()

    prefix = "a"
    suf = suffixes(root, prefix)
    for s in suf:
        print(prefix+s)
