"""
A HashTable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

class HashTable:
    def __init__(self, nbuckets):
        """Init with a list of nbuckets lists"""
        self.buckets = [[] for i in range(nbuckets)]


    def __len__(self):
        n = 0
        for i in range(len(self.buckets)):
            n += len(self.buckets[i])
        return n


    def __setitem__(self, key, value):
        """
        Perform the equivalent of table[key] = value
        Find the appropriate bucket indicated by key and then append (key,value)
        to that bucket if the (key,value) pair doesn't exist yet in that bucket.
        If the bucket for key already has a (key,value) pair with that key,
        then replace the tuple with the new (key,value).
        Make sure that you are only adding (key,value) associations to the buckets.
        The type(value) can be anything. Could be a set, list, number, string, anything!
        """
        h = self.hashcode(key) % len(self.buckets)
        # find existing
        el = self.bucket_indexof(key)
        # print(f"{key} in bucket {h} element {el}")
        assoc = (key, value)
        if el is not None: # replace
            self.buckets[h][el] = assoc
        else:
            self.buckets[h].append(assoc)


    def __getitem__(self, key):
        """
        Return the equivalent of table[key].
        Find the appropriate bucket indicated by the key and look for the
        association with the key. Return the value (not the key and not
        the association!). Return None if key not found.
        """
        h = self.hashcode(key) % len(self.buckets)
        i = self.bucket_indexof(key)
        if i is not None:
            (k,v) = self.buckets[h][i]
            return v
        return None


    def __contains__(self, key):
        return self[key] is not None


    def __iter__(self):
        return (key for key in self.keys())
        pass


    def keys(self):
        elems = []
        for i in range(len(self.buckets)):
            elems.extend( [key for key,value in self.buckets[i]] )
        return elems


    def items(self):
        elems = []
        for i in range(len(self.buckets)):
            elems.extend( self.buckets[i] )
        return elems


    def __repr__(self):
        """
        Return a string representing the various buckets of this table.
        The output looks like:
            0000->
            0001->
            0002->
            0003->parrt:99
            0004->
        where parrt:99 indicates an association of (parrt,99) in bucket 3.
        """
        s = ""
        for i in range(len(self.buckets)):
            bucketlist = self.buckets[i]
            s += "%04d" % i + "->"
            bucket = [str(k)+":"+str(v) for (k,v) in bucketlist]
            s += ", ".join(bucket) + "\n"
        return s


    def __str__(self):
        """
        Return what str(table) would return for a regular Python dict
        such as {parrt:99}. The order should be in bucket order and then
        insertion order within each bucket. The insertion order is
        guaranteed when you append to the buckets in htable_put().
        """
        assocs = []
        for i in range(len(self.buckets)):
            bucketlist = self.buckets[i]
            bucket = [str(k)+":"+str(v) for (k,v) in bucketlist]
            assocs.extend(bucket)
        return "{" + ", ".join(assocs) + "}"


    def hashcode(self, o):
        """
        Return a hashcode for strings and integers; all others return None
        For integers, just return the integer value.
        For strings, perform operation h = h*31 + ord(c) for all characters in the string
        """
        if isinstance(o, str):
            h = 0
            for c in o:
                h = h*31 + ord(c)
            return h
        elif isinstance(o, int):
            return o
        return None

    def bucket_indexof(self, key):
        """
        You don't have to implement this, but I found it to be a handy function.

        Return the index of the element within a specific bucket; the bucket is:
        table[hashcode(key) % len(table)]. You have to linearly
        search the bucket to find the tuple containing key.
        """
        h = self.hashcode(key) % len(self.buckets)
        bucket = self.buckets[h]
        el = None
        for i in range(len(bucket)):
            (k, v) = bucket[i]
            if k == key:
                el = i
        return el
