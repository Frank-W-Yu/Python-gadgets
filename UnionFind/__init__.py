'''
This Module implements multiple union find algorithms. It unions n numbers between 0 and n-1.
If the input values are not between 0 and n-1, an extra mapping table is needed.
Author: Weijie Yu
Date: 06/21/2018
'''

class quick_find(object):
    '''
    Quick find algorithm, during unite, it iterates all elements and re-assigns to the new common value when the
    elements are in the same union, while for find it just needs check if the values are equal.
    Time complexity:
    Find: O(1)
    Union: O(n)
    '''
    def __init__(self, n):
        self.nums = range(n)

    def unite(self, p, q):
        pid = self.nums[p]
        for i, n in enumerate(self.nums):
            if n == pid:
                self.nums[i] = q

    def find(self, p, q):
        return self.nums[p] == self.nums[q]

class quick_union(object):
    '''
    Quick union algorithm, for both unite and find operations, it needs to find the root nodes first and then unites or
    compares the root nodes
    Time complexity:
    Find: O(N)
    Union: O(N)
    '''

    def __init__(self, n):
        self.nums = range(n)

    def root(self, p):
        while self.nums[p] != p:
            p = self.nums[p]
        return p

    def unite(self, p, q):
        self.nums[self.root(p)] = self.root(q)

    def find(self, p, q):
        return self.root(p) == self.root(q)

class weighted_quick_union(object):
    '''
    Weighted quick union algorithm: similar to quick union, it also tracks the height of union tree and alwasy unite the
    smaller tree to the bigger tree
    Time complexity:
    Find: O(N)
    Union: O(N)
    '''

    def __init__(self, n):
        self.nums = range(n)
        self.size = [1] * n

    def root(self, p):
        while self.nums[p] != p:
            p = self.nums[p]
        return p

    def unite(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if self.size[i] < self.size[j]:
            self.nums[i] = j
            self.size[j] += self.size[i]
        else:
            self.nums[j] = i
            self.size[i] += self.size[j]

    def find(self, p, q):
        return self.root(p) == self.root(q)

class path_compression_quick_union(object):
    '''
    Path compression quick union algorithm: similar to quick union, it adds path compression in root method
    Time complexity:
    Find: O(N)
    Union: O(N)
    '''

    def __init__(self, n):
        self.nums = range(n)

    def root(self, p):
        while self.nums[p] != p:
            self.nums[p] = self.nums[self.nums[p]]
            p = self.nums[p]
        return p

    def unite(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if self.size[i] < self.size[j]:
            self.nums[i] = j
            self.size[j] += self.size[i]
        else:
            self.nums[j] = i
            self.size[i] += self.size[j]

    def find(self, p, q):
        return self.root(p) == self.root(q)
