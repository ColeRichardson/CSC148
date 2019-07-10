class A: # WRITE THE OUTPUT BELOW HERE:
    def __init__(self, x):
        self.x = x
    def double_x(self):
        self.x = self.x * 2
class B(A):
    def __init__(self, y):
        self.y = y
    def double_y(self):
        self.y = self.y * 2
class C(B):
    pass
if __name__ == "__main__":
    a = A(1)
    b = B(2)
    c = C(3)
    try:
        print("a.x =", a.x)
        print("b.y =", b.y)
        print("b.x =", b.x)
    except:
        print("bad!")
    try:
        b.double_y()
    except IOError:
        print("bad again!")
    finally:
        print("finally")
    try:
        print("final a =", a.x)
        print("final b =", b.y)
        print("final c =", c.y)
    except:
        print("still bad!")
    print("It’s all good")
