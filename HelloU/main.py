# Working with advanced Sets

s = set()
s.add(1)
s.add(2)
s.add(1)
sc = s.copy()
s.add(4)
print(s)
print(sc)
print(s.difference(sc))
set1 = {1, 2, 3}
set2 = {1, 4, 5}
print(set1.difference_update(set2), '\n', set1, '\n', set2)
set2.discard(5)
print(set2)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)


s1 = {1, 2}
s2 = {1, 2, 4}
s3 = {5}

print(s1.isdisjoint(s3))
print(s1.issubset(s2))
print(s2.issuperset(s1))

s1 = {1, 2}
s2 = {1, 2, 4}
s1.update(s2)
print(s1, s2)
