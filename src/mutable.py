class DA_mut(object):
    def __init__(self, l=[]):
        self.s = 0
        self.l = [None for i in range(100)]
        for i in range(len(l)):
            self.l[i] = l[i]

    def __str__(self):
        return " : ".join(map(str, self.to_list()))

    @property
    def size(self):
        self.s = 0
        for value in self.l:
            if value is None:
                return self.s
            else:
                self.s += 1
        return self.s

    def to_list(self):
        lst = []
        for value in self.l:
            if value is not None:
                lst.append(value)

        return lst

    def from_list(self, lst):
        for i in range(len(lst)):
            self.l[i] = lst[i]

    def add_to_head(self, value):
        lst = [value]
        for i in range(len(self.l) - 1):
            lst.append(self.l[i])
        self.l = lst

    def add_to_tail(self, value):
        for i in range(len(self.l)):
            if self.l[i] is None:
                self.l[i] = value
                break

    def map(self, f):
        for i in range(self.size):
            if self.l[i] is not None:
                self.l[i] = f(self.l[i])

    def reduce(self, f, initial_state):
        state = initial_state
        cur = 0
        while self.l[cur] is not None:
            state = f(state, self.l[cur])
            cur += 1
        return state

    def find(self, value):
        for v in self.to_list():
            if v is value:
                return True
        return False

    def filter(self, value):
        lst_filter = []
        for i in self.l[:self.size]:
            if i is not value:
                lst_filter.append(i)
        return lst_filter

    def mempty(self):
        self.l = [None for i in range(100)]

    def mconcat(self,DA2):
        i = 0
        for e in DA2:
            self.l[self.size + i ] = e

    def remove(self,value):
        new = [None for i in range(100)]
        num = 0
        for i in range(self.size):
            if i is not value:
                new[num] = self.l[i]
                num += 1
        self.l = new

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
