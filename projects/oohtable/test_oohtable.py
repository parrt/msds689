from oohtable import *
import pandas as pd

def test_empty():
    table = HashTable(5)
    assert str(table) == "{}"


def test_single():
    table = HashTable(5)
    table["parrt"] = 99
    assert str(table) == "{parrt:99}"


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


def test_int_to_int():
    table = HashTable(5)
    for i in range(1, 11):
        table[i] = i
    s = str(table)
    assert s=="{5:5, 10:10, 1:1, 6:6, 2:2, 7:7, 3:3, 8:8, 4:4, 9:9}"


def test_str_to_str():
    table = HashTable(5)
    table["a"] = "x"
    table["b"] = "y"
    table["c"] = "z"
    table["f"] = "i"
    table["g"] = "j"
    table["k"] = "k"
    s = str(table)
    s = '{'+ ', '.join(sorted(s[1:-1].split(', '))) +'}' # sort elements
    assert s=='{a:x, b:y, c:z, f:i, g:j, k:k}', "found "+s


def test_str_to_list():
    table = HashTable(5)
    table["parrt"] = [2, 99, 3942]
    table["tombu"] = [6, 3, 1024, 99, 102342]
    s = str(table)
    assert table['parrt']==[2, 99, 3942]
    assert table['tombu']==[6, 3, 1024, 99, 102342]


def test_replace_str():
    table = HashTable(5)
    table["a"] = "x"
    table["b"] = "y"
    table["a"] = "z"
    table["a"] = "i"
    table["g"] = "j"
    table["g"] = "k"
    s = str(table)
    s = '{'+ ', '.join(sorted(s[1:-1].split(', '))) +'}' # sort elements
    assert s == '{a:i, b:y, g:k}', "found " + s


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
        keys.append(str(k))
    assert sorted(keys)==['100', 'a', 'b', 'parrt']


def test_keys0():
    table = HashTable(5)
    assert table.keys()==[]


def test_keys():
    table = HashTable(5)
    table["a"] = "x"
    table["b"] = "y"
    table['z'] = ['tom','mary']
    table["parrt"] = {99}
    assert sorted(table.keys())==['a', 'b', 'parrt', 'z']


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
    # Use student HashTable
    h = HashTable(101)
    for w in words:
        if w not in h:
            h[w] = 0
        h[w] = h[w] + 1

    # Test using dataframe
    df = pd.DataFrame(data=list(h.items()), columns=['word','count'])
    df = df.sort_values(['count','word'], ascending=[False,True])
    assert str(df.values)==\
"""[['and' 9]
 ['the' 9]
 ['i' 8]
 ['as' 5]
 ['in' 4]
 ['a' 3]
 ['one' 3]
 ['that' 3]
 ['ages' 2]
 ['be' 2]
 ['both' 2]
 ['could' 2]
 ['diverged' 2]
 ['for' 2]
 ['had' 2]
 ['it' 2]
 ['not' 2]
 ['roads' 2]
 ['to' 2]
 ['took' 2]
 ['two' 2]
 ['wood,' 2]
 ['about' 1]
 ['all' 1]
 ['another' 1]
 ['back.' 1]
 ['because' 1]
 ['bent' 1]
 ['better' 1]
 ['black.' 1]
 ['by' 1]
 ['by,' 1]
 ['claim,' 1]
 ['come' 1]
 ['day!' 1]
 ['difference.' 1]
 ['doubted' 1]
 ['down' 1]
 ['equally' 1]
 ['ever' 1]
 ['fair,' 1]
 ['far' 1]
 ['first' 1]
 ['frost' 1]
 ['grassy' 1]
 ['has' 1]
 ['having' 1]
 ['hence:' 1]
 ['how' 1]
 ['i-' 1]
 ['if' 1]
 ['just' 1]
 ['kept' 1]
 ['knowing' 1]
 ['lay' 1]
 ['leads' 1]
 ['leaves' 1]
 ['less' 1]
 ['long' 1]
 ['looked' 1]
 ['made' 1]
 ['morning' 1]
 ['no' 1]
 ['oh,' 1]
 ['on' 1]
 ['other,' 1]
 ['passing' 1]
 ['perhaps' 1]
 ['really' 1]
 ['road' 1]
 ['robert' 1]
 ['same,' 1]
 ['shall' 1]
 ['should' 1]
 ['sigh' 1]
 ['somewhere' 1]
 ['sorry' 1]
 ['step' 1]
 ['stood' 1]
 ['taken' 1]
 ['telling' 1]
 ['them' 1]
 ['then' 1]
 ['there' 1]
 ['this' 1]
 ['though' 1]
 ['travel' 1]
 ['traveled' 1]
 ['traveler,' 1]
 ['trodden' 1]
 ['undergrowth;' 1]
 ['wanted' 1]
 ['was' 1]
 ['way' 1]
 ['way,' 1]
 ['wear;' 1]
 ['where' 1]
 ['with' 1]
 ['worn' 1]
 ['yellow' 1]
 ['yet' 1]]"""
