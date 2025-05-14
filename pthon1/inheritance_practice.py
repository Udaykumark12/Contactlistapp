
a = 1
b = 2
c = 3
d = 4
e = 5


class A:
    def m1(self):
        print(a + b)
        return a+b

class B:
    def m2(self):
        print(c + d)
        return self

class C:
    def m3(self):
        print(d + e)
        return self


# Create objects of the classes
obj_a = A().m1()
obj_b = B().m2()
obj_c = C().m3()

# Call the methods
# obj_a.m1()  # Output: 3
# obj_b.m2()  # Output: 7
# obj_c.m3()  # Output: 9
