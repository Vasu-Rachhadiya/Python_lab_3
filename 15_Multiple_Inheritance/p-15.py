class a:
    def __init__(self, i):
        self.i = i
class b:
    def __init__(self, j):
        self.j = j
class c(a, b):
    def __init__(self, i, j, k):
        a.__init__(self, i)
        b.__init__(self, j)
        self.k = k
    def dis(self):
        print(self.i * self.j * self.k)
c1 = c(10, 20, 30)
c1.dis()