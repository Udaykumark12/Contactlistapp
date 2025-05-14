# class A:
#     def uday(self,x,y):
#         self.x, self.y = x,y
#
#
#     def nirmal(self):
#
#         c,d=10,20
#         print(self.x+c)
#
# b = A()
# b.uday(10,20)
# b.nirmal()
#

# class A:
#     def uday(self):
#         self.a, self.b = 10, 20  # Initialize a and b with fixed values
#
#     def nirmal(self):
#         b.uday()
#         c, d = 40, 20
#         print(self.a + c)  # Use self.a which was set in uday()
#
# b = A()
# b.nirmal()


from select import select


# b.nirmal()  # This works because self.a is initialized

# class A:
#     def __init__(self):  # Constructor
#         self.a = 10
#         self.b = 20
#
#     def nirmal(self):
#         c, d = 10, 20
#         print(self.a + c)  # self.a is already set in constructor
#
# b = A()
# b.nirmal()



# def a():
#     x=10
#     y=20
#     return x+y
#
# def b():
#     z=a()
#     print(z)
#
# b()







# n=5
# for i in range(n):
#     for j in range(i):
#         print("* ",end='')
#     print()

#
# n=5
# for i in range(n):
#     for k in range(n-i):
#         print("",end=' ')
#     for j in range(i):
#         print("* ", end='')
#     print()




