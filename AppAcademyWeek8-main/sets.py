# --- Sets--- #

# Create a set
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: all elements from both sets (no duplicates)
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection: only elements common to both sets
inter_set = set1.intersection(set2)
print("Intersection:", inter_set)

# Difference
diff_set = set1.difference(set2)
print("Difference", diff_set)