import time
import random
import copy
'''
Jest to program mający na celu porównanie argorytmów sortujących, jeśli chcemy sprawdzic tylko niektóre algorytmy,
należy wtedy wykomentować te, które nas nie interesują(Na samym dole kodu).W 9 linijce możemy zmienić zakres 
danych na taki, jaki nas interesuje. 
'''
X=[random.randint(1, 50) for i in range(5)]
#X.sort #ustawia rozkład rosnący
B = copy.deepcopy(X)
C = copy.deepcopy(X)
D = copy.deepcopy(X)
E = copy.deepcopy(X)
F = copy.deepcopy(X)
G = copy.deepcopy(X)
H = copy.deepcopy(X)
def BS(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

def SS(A):
    for i in range(len(A)):
        minimum = i
        for j in range(i+1, len(A)):
            if A[j] < A[minimum]:
                minimum = j
        A[minimum], A[i] = A[i],  A[minimum]
    return A

def IS(A):
    for i in range(1,len(A)):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j -1
        A[j+1] = key
    return A
def MS(A):
    if len(A) > 1:
        mid = len(A) // 2
        L= A[:mid]
        R = A[mid:]
        MS(L)
        MS(R)
        l = r = i = 0
        while l < len(L) and r < len(R):
            if L[l] > R[r]:
                A[i] = R[r]
                r += 1
            else:
                A[i] = L[l]
                l += 1
            i += 1
        while r < len(R):
            A[i] = R[r]
            r += 1
            i += 1
        while l < len(L):
            A[i] = L[l]
            l += 1
            i += 1
    return A

def CS(A):
    cntr = [0]*(max(A)+1)
    for el in A:
        cntr[el] += 1
    for i in range(1,len(cntr)):
        cntr[i] += cntr[i-1]
    result = [0]*len(A)
    for el in A:
        i = cntr[el] - 1
        result[i] = el
        cntr[el] -= 1
    return result

def QSSk(A):
    if len(A) < 2:
        return A
    else:
        mniejsz = []
        wieksz = []
        pivot = A[len(A)-1]
        for el in A[0:(len(A)-1)]:
            if el < pivot:
                mniejsz.append(el)
            else:
                wieksz.append(el)
        return QSSk(mniejsz) + [pivot] + QSSk(wieksz)

def QSSr(A):
    if len(A) < 2:
        return A
    else:
        mniejsz = []
        wieksz = []
        pivot = A[len(A)//2]
        for el in A[0:(len(A)//2)]:
            if el < pivot:
                mniejsz.append(el)
            else:
                wieksz.append(el)
        for el in A[(len(A)//2+1):]:
            if el < pivot:
                mniejsz.append(el)
            else:
                wieksz.append(el)
        return QSSr(mniejsz) + [pivot] + QSSr(wieksz)

def HS(A):
    def kopcowanie(A, n, i):
        najw = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and A[i] < A[l]:
            najw = l
        if r < n and A[najw] < A[r]:
            najw = r
        if najw != i:
            A[i],A[najw] = A[najw],A[i]
            kopcowanie(A, n, najw)

    n = len(A)
    for i in range(n//2 - 1, -1, -1):
        kopcowanie(A, n, i)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        kopcowanie(A, i, 0)

    return A

start = time.time()
print(BS(X))
finish = time.time()
print(f"BS posortował to w czasie: {(finish-start):.20f}")

start = time.time()
print(SS(B))
finish = time.time()
print(f"SS posortował to w czasie: {(finish-start):.20f}")


start = time.time()
print(IS(C))
finish = time.time()
print(f"IS posortował to w czasie: {(finish-start):.20f}")

start = time.time()
print(MS(D))
finish = time.time()
print(f"MS posortował to w czasie: {(finish-start):.20f}")

start = time.time()
print(CS(E))
finish = time.time()
print(f"CS posortował to w czasie: {(finish-start):.20f}")

start = time.time()
print(QSSk(F))
finish = time.time()
print(f"QS z skrajnym pivotem posortował to w czasie: {(finish-start):.20f}")

start = time.time()
print(QSSr(G))
finish = time.time()
print(f"QS z środkowym pivotem posortował to w czasie: {(finish-start):.20f}")

start = time.time()
print(HS(H))
finish = time.time()
print(f"HS posortował to w czasie: {(finish-start):.20f}")
