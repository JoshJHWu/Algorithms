#debuggers
import code #code.interact(local=locals())
from IPython import embed #embed()

def mergesort(arr):
    print("splitting",arr)
    if len(arr) == 1:
        return arr
    mid = len(arr)/2
    l = mergesort(arr[:mid])
    r = mergesort(arr[mid:])
    return merge(l,r)

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
        print("merging", result + l[i:])
        return result + l[i:]
    if j != len(r):
        print("merging", result + r[j:])
        return result + r[j:]


print mergesort([1,7,4,6,2])
# print merge([2,7],[5])
