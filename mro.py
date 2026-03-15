class A:
    def __init__(self):
        self.x = 10
        

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 20
       
class C(A):
    def __init__(self):
        super().__init__()
        self.z = 30

class D(C,B):
    pass

d1 = D()
print(d1.x, d1.y, d1.z)
