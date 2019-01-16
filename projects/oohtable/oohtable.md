# OO Search Engine Implementation

In [MSDS962](https://github.com/parrt/msds692/blob/master/hw/search.md) you learned how to create and use a hash table. You did so by using non-object-oriented programming; i.e., just a bunch of functions. In this homework, your will build an object-oriented version of your hash table by updating your original code base. You will see that the object-oriented version is much more user-friendly and that it behaves very much like the built-in `dict` class.

As you work on this project, working from your previous codebase, I encourage you reflect on:

* How easy is it to understand your code a few months later? 
* Do you regret not adding more comments?
* Would you use different variable names now?
* Could you improve your code, given your enhanced experience?

## Discussion and requirements

Using the hash table you created in MSDS692 was a bit awkward. For example, here is how we created a hash table with 5 buckets and stored 99 at the key `parrt`:

```python
table = htable(5)
htable_put(table, "parrt", 99)
```

For this project, you are going to build a class definition called `HashTable` in file `oohtable.py` so that we can say the following instead:

```python
table = HashTable(5)
table["parrt"] = 99
```

Similarly, to fetch something out of the table, we used to have to say:

```python
x = htable_get(table, "parrt")
```

But, now we can use the indexing operator:

```python
x = table["parrt"]
```

Your implementation of `HashTable` must define methods `__setitem__` and `__getitem__` to implement these operators (see operator overloading discussion).

To count the elements within the hash table we want to be able to use `len(table)`. To do that, you have to implement the `__len__` method. Note this is counting the number of elements among all of the buckets, not the number of buckets.

To iterate through the keys of your hash table like this:

```python
for k in table:
    print(k)
```

you need to implement the `__iter__` method.  That method can return a so-called generator expression that iterates over the `keys()`.

To test for membership of a key like this:

```
if 'parrt' in table:
    print("woot!")
```

you must implement `__contains__`.

To get a list of the keyvalue pairs as tuples like `[('the', 9), ('and', 9), ...]`, implement the `items` method.

As with a built-in dictionary from Python, converting something to string using `str(table)` or just `print(table)` should also work. That means you have to implement the `__str__` method to print out the key:value pairs. We also had a method that dumped out all the buckets for debugging purposes called `htable_buckets_str()`.  Instead, we use `__repr__` with the class definition to print out a representation of that object.

Here are all of the methods that you must implement in the class definition:

<img src="images/oohtable-methods.png" width="220">

Of course you can implement other methods, but those are the ones used by the test rig. (My class also has `hashcode()`, for example.)

Please note that you cannot have any global variables, variable sitting outside of your class or method definitions. You can only have local variables, parameters of functions, and fields of the `HashTable` class.

Your `oohtable.py` file also should not have code that gets executed when other files import `oohtable.py`.

The tests described in the next section should execute very quickly, as in less than a second.

## Evaluation

To evaluate your projects, we will run the unit tests.  The unit tests I have provided for you test all of the functions described above. Because they all use the index notation, `table[key]`, you should get `__setitem__` and `__getitem__` working first.

We will grade in a binary fashion (works or doesn't) because you have all of the known tests.

Please make a copy of [test_oohtable.py](test_oohtable.py) in the same directory as your `oohtable.py` file and then run your tests either from your development environment or the command line. Ultimately, you want the test results to look like the following:

```
$ python -m pytest -v test_oohtable.py 
======================================== test session starts =========================================
platform darwin -- Python 3.6.7, pytest-3.8.0, py-1.6.0, pluggy-0.7.1 -- /Users/parrt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/parrt/courses/msds689-private/projects/oohtable, inifile:
plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
collected 18 items                                                                                   

test_oohtable.py::test_empty PASSED                                                            [  5%]
test_oohtable.py::test_single PASSED                                                           [ 11%]
test_oohtable.py::test_get0 PASSED                                                             [ 16%]
test_oohtable.py::test_get PASSED                                                              [ 22%]
test_oohtable.py::test_singleton PASSED                                                        [ 27%]
test_oohtable.py::test_int_to_int PASSED                                                       [ 33%]
test_oohtable.py::test_str_to_str PASSED                                                       [ 38%]
test_oohtable.py::test_str_to_list PASSED                                                      [ 44%]
test_oohtable.py::test_replace_str PASSED                                                      [ 50%]
test_oohtable.py::test_len0 PASSED                                                             [ 55%]
test_oohtable.py::test_len PASSED                                                              [ 61%]
test_oohtable.py::test_items0 PASSED                                                           [ 66%]
test_oohtable.py::test_items PASSED                                                            [ 72%]
test_oohtable.py::test_iter0 PASSED                                                            [ 77%]
test_oohtable.py::test_iter PASSED                                                             [ 83%]
test_oohtable.py::test_keys0 PASSED                                                            [ 88%]
test_oohtable.py::test_keys PASSED                                                             [ 94%]
test_oohtable.py::test_wordfreq PASSED                                                         [100%]

===================================== 18 passed in 0.08 seconds ======================================
```

## Deliverables

You must complete and add the following file to the root of your `oohtable-`*userid* repository in the USF-MSDS689 organization.

* `oohtable.py`


