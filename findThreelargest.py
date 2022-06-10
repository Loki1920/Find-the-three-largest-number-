#Python program to find largest three in a array
def largest(arr):
  if len(arr)>=3:
    t=[]
    for i in range(3):
      m = max(arr)
      t.append(m)
      arr.remove(m)
  return t[::-1]

k = [141,1,17,-7,-17,-27,18,541,6,7,7]
print(largest(k))

