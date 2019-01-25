from oohtable import *

def test_empty():
    table = HashTable(5)
    assert str(table) == "{}"
    assert table.__repr__() == """0000->
0001->
0002->
0003->
0004->
"""


def test_single():
    table = HashTable(5)
    table["parrt"] = 99
    assert str(table) == "{parrt:99}"
    assert table.__repr__() == """0000->
0001->
0002->
0003->parrt:99
0004->
"""


def test_get0():
    table = HashTable(5)
    assert table['parrt'] == None


def test_get():
    table = HashTable(5)
    table["parrt"] = 99
    assert table['parrt'] == 99


def test_singleton():
    table = HashTable(5)
    table["parrt"] = {99}
    assert str(table) == "{parrt:{99}}"
    assert table.__repr__() == """0000->
0001->
0002->
0003->parrt:{99}
0004->
"""


def test_int_to_int():
    table = HashTable(5)
    for i in range(1, 11):
        table[i] = i
    s = str(table)
    assert s=="{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"
    s = table.__repr__()
    assert s == """0000->5:5, 10:10
0001->1:1, 6:6
0002->2:2, 7:7
0003->3:3, 8:8
0004->4:4, 9:9
"""


def test_str_to_str():
    table = HashTable(5)
    table["a"] = "x"
    table["b"] = "y"
    table["c"] = "z"
    table["f"] = "i"
    table["g"] = "j"
    table["k"] = "k"
    s = str(table)
    assert s=='{a:x, f:i, k:k, b:y, g:j, c:z}', "found "+s
    s = table.__repr__()
    assert s == """0000->
0001->
0002->a:x, f:i, k:k
0003->b:y, g:j
0004->c:z
"""


def test_str_to_list():
    table = HashTable(5)
    table["parrt"] = [2, 99, 3942]
    table["tombu"] = [6, 3, 1024, 99, 102342]
    assert str(table) == "{tombu:[6, 3, 1024, 99, 102342], parrt:[2, 99, 3942]}"
    assert table.__repr__() == """0000->
0001->tombu:[6, 3, 1024, 99, 102342]
0002->
0003->parrt:[2, 99, 3942]
0004->
"""

def test_replace_str():
    table = HashTable(5)
    table["a"] = "x"
    table["b"] = "y"
    table["a"] = "z"
    table["a"] = "i"
    table["g"] = "j"
    table["g"] = "k"
    s = str(table)
    assert s == '{a:i, b:y, g:k}', "found " + s
    s = table.__repr__()
    assert s == """0000->
0001->
0002->a:i
0003->b:y, g:k
0004->
"""

def test_len0():
    table = HashTable(5)
    assert len(table)==0


def test_len():
    table = HashTable(5)
    table["a"] = "x"
    table["b"] = "y"
    table["a"] = "z"
    table["a"] = "i"
    table["g"] = "j"
    table["g"] = "k"
    assert len(table)==3


def test_items0():
    table = HashTable(500)
    assert str(table.items())=="[]"


def test_items():
    table = HashTable(5)
    table["parrt"] = {99}
    assert str(table.items())=="[('parrt', {99})]"


def test_iter0():
    table = HashTable(5)
    keys = []
    for k in table:
        keys.append(k)
    assert str(keys)=="[]"


def test_iter():
    table = HashTable(5)
    table["a"] = "x"
    table["b"] = "y"
    table[100] = ['tom','mary']
    table["parrt"] = {99}
    keys = []
    for k in table:
        keys.append(k)
    assert keys==[100, 'a', 'b', 'parrt']


def test_keys0():
    table = HashTable(5)
    assert table.keys()==[]


def test_keys():
    table = HashTable(5)
    table["a"] = "x"
    table["b"] = "y"
    table[100] = ['tom','mary']
    table["parrt"] = {99}
    assert table.keys()==[100, 'a', 'b', 'parrt']


def test_wordfreq():
    text = """
    The Road Not Taken by Robert Frost
    
    Two roads diverged in a yellow wood,
    And sorry I could not travel both
    And be one traveler, long I stood
    And looked down one as far as I could
    To where it bent in the undergrowth;
    Then took the other, as just as fair,
    And having perhaps the better claim,
    Because it was grassy and wanted wear;
    Though as for that the passing there
    Had worn them really about the same,
    And both that morning equally lay
    In leaves no step had trodden black.
    Oh, I kept the first for another day!
    Yet knowing how way leads on to way,
    I doubted if I should ever come back.
    I shall be telling this with a sigh
    Somewhere ages and ages hence:
    Two roads diverged in a wood, and I-
    I took the one less traveled by,
    And that has made all the difference.
    """
    words = text.lower().split()
    h = HashTable(101)
    for w in words:
        if w not in h:
            h[w] = 0
        h[w] = h[w] + 1
    s = str(sorted(h.items(), key=lambda kv: kv[1], reverse=True)) # convert to counter to normalize; needs __iter__() to work
    assert s == """[('the', 9), ('and', 9), ('i', 8), ('as', 5), ('in', 4), ('that', 3), ('one', 3), ('a', 3), ('be', 2), ('diverged', 2), ('had', 2), ('ages', 2), ('two', 2), ('it', 2), ('roads', 2), ('could', 2), ('took', 2), ('to', 2), ('for', 2), ('wood,', 2), ('not', 2), ('both', 2), ('black.', 1), ('hence:', 1), ('bent', 1), ('them', 1), ('by,', 1), ('then', 1), ('passing', 1), ('back.', 1), ('perhaps', 1), ('travel', 1), ('sigh', 1), ('on', 1), ('less', 1), ('all', 1), ('was', 1), ('leads', 1), ('wanted', 1), ('morning', 1), ('robert', 1), ('about', 1), ('way', 1), ('if', 1), ('undergrowth;', 1), ('knowing', 1), ('by', 1), ('step', 1), ('kept', 1), ('sorry', 1), ('other,', 1), ('this', 1), ('made', 1), ('really', 1), ('telling', 1), ('yellow', 1), ('road', 1), ('far', 1), ('fair,', 1), ('wear;', 1), ('stood', 1), ('better', 1), ('doubted', 1), ('day!', 1), ('yet', 1), ('there', 1), ('has', 1), ('should', 1), ('somewhere', 1), ('just', 1), ('oh,', 1), ('worn', 1), ('same,', 1), ('difference.', 1), ('lay', 1), ('claim,', 1), ('leaves', 1), ('another', 1), ('long', 1), ('because', 1), ('i-', 1), ('come', 1), ('traveled', 1), ('equally', 1), ('first', 1), ('where', 1), ('grassy', 1), ('how', 1), ('down', 1), ('way,', 1), ('frost', 1), ('shall', 1), ('no', 1), ('ever', 1), ('having', 1), ('traveler,', 1), ('though', 1), ('taken', 1), ('trodden', 1), ('with', 1), ('looked', 1)]"""
