#debuggers
import code #code.interact(local=locals())
from IPython import embed #embed()

def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)/2
    l = mergesort(arr[0:mid])
    r = mergesort(arr[mid:])
    merge(l,r)

def merge(l,r):
    i = 0
    j = 0
    result = []
    while i <= len(l) - 1 and j <= len(r) - 1:
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    if i != len(l):
        return result + l[i:]
    if j != len(r):
        return result + r[j:]


print mergesort([1,7,4,6,2])
# print merge([1,4,3],[2,5])
