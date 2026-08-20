#Array Insertion COde1
def insert(a, ind, b):
  a.append(None)
  i = len(a)-2
  while i>= ind:
    a[i+1] = a[i]
    i-=1
  a[ind] = b
  return b

p = [101, 102, 104]
insert(p, 2, 103)
print("Array post Insertion", p)
