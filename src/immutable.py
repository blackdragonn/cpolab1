def size(n):
    s = 0
    if(n is not None):
        for e in n:
            if e is not None:
                s += 1
    return s


def to_list(n):
    lst = []
    for e in n:
        lst.append(e)
    return lst


def from_list(lst):
    n = DA_imm([])
    for i in range(len(lst)):
        n.l[i] = lst[i]
    return n


def add_to_head(n, value):
    l = [value]
    for i in range(1, 100):
        if n.l[i - 1] is not None:
            l.append(n.l[i - 1])
    return DA_imm(l)


def add_to_tail(n, value):
    for i in range(100):
        if n.l[i] is None:
            n.l[i] = value
            return n


def find(n, value):
    for e in n:
        if e is value:
            return True
    return False


def remove(n, value):
    l = []
    for i in range(size(n)):
        if i is not value:
            l.append(n.l[i])
    return DA_imm(l)


def filter(n, value):
    l = []
    for e in n:
        if e is not value:
            l.append(e)
    return DA_imm(l)


def map(n, f):
    l = []
    for e in n:
        l.append(f(e))
    return DA_imm(l)


def reduce(n, f, initial_state):
    state = initial_state
    cur = 0
    while n.l[cur] is not None:
        state = f(state, n.l[cur])
        cur += 1
    return state


def mempty():
    return DA_imm()


def mconcat(a, b):
    l1 = to_list(a)
    l2 = to_list(b)
    return DA_imm(l1 + l2)

def iterator(lst):
    length=size(lst)
    da = lst
    index=0
    def foo():
        nonlocal da
        nonlocal length
        nonlocal index
        if ((index >= length) | (da is None)) : raise StopIteration
        tmp = da.l[index]
        index=index+1
        return tmp
    return foo

class DA_imm(object):
    def __init__(self, l=[]):
        self.l = [None for i in range(100)]
        for i in range(len(l)):
            self.l[i] = l[i]

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.l[self.a] is not None:
            x = self.l[self.a]
            self.a += 1
            return x
        else:
            raise StopIteration
    
    def __eq__(self, other):
        for i in range(100):
            if self.l[i] != other.l[i]:
                return False
        return True