from lolviz import *
import time
import os
import psutil

class TrieNode:
    def __init__(self):
        self.edges = [] # init edges, one per a..z letter
        for c in range(ord('a'), ord('z')+1): self.edges.append(None)


def add(p:TrieNode, s:str, i=0) -> None:
    if i>=len(s): return
    e = ord(s[i]) - ord('a')
    if p.edges[e] is None:
        p.edges[e] = TrieNode()
    add(p.edges[e], s, i+1)


def search(root:TrieNode, s:str, i=0) -> bool:
    "Return true if s is prefix of word in Trie or full word in Trie"
    p = root
    while p is not None:
        if i>=len(s): return True
        e = ord(s[i]) - ord('a')
        if p.edges[e] is None: return False
        p = p.edges[e]
        i += 1
    return True


def brute_force_search(words):
    start = time.time()
    found = 0
    for w in words:
        if w in words:
            found += 1
    print(f"{found} found out of {len(words)}")
    stop = time.time()
    print(f"Brute force search time {stop-start:.2f}s") # wow: 265.85s (4.43 minutes)


def create_trie(words):
    start = time.time()
    root = TrieNode()
    for w in words:
        w = w.strip().lower()
        if w.isalpha():
            add(root, w)
    stop = time.time()
    print(f"TRIE build time {stop-start:.2f}s") # 6s
    return root


def trie_search(words):
    start = time.time()
    found = 0
    for w in words:
        w = w.strip().lower()
        if w.isalpha():
            if search(root, w):
                found += 1

    print(f"{found} found out of {len(words)}")
    stop = time.time()
    print(f"TRIE search time {stop-start:.2f}s")  # wow: 265.85s (4.43 minutes)


def load():
    with open("/usr/share/dict/words") as f:  # linux likely /usr/dict/words
        words = f.readlines()
    return words


if __name__ == '__main__':
    words = load()
    #words = words[:12000] # reduce size of word list during development
    print(f"{len(words)} words in dictionary")

    process = psutil.Process(os.getpid())
    print(f"{process.memory_info().rss/1024**2:,.3f} MB in use before creating TRIE")

    root = create_trie(words)

    process = psutil.Process(os.getpid())
    print(f"{process.memory_info().rss/1024**2:,.3f} MB in use after creating TRIE")

    trie_search(words)

    #objviz(root).view()