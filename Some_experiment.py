#!/usr/bin/env python


alist = ['a', 'b', 'c', 'd','e']

for i in range (0, 3):
    print i
    print alist[i]

# We are quoting the indexes, it simply doesn't include the last one!
print alist[:3]   # ['a', 'b', 'c']
print alist[0:3]  # ['a', 'b', 'c']
print alist[1:3]  # ['b', 'c']

print alist[0:3:1]





