from itertools import count

# my_string="ChatGPT helps you get answers, find inspiration and be more productive. It is free to use and easy to try. Just ask and ChatGPT can help with writing"
# b={}
# for i in my_string.lower():
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
#
# print(b)

# a=float(input("enter a number"))
# b=float(input("enter second number"))
# c=a+b
# print(c)


# l =[]
# r =[]
# for i in range(100):
#     if i%2==1:
#         l.append(i)
#     else:
#         r.append(i)
# print(l)
# print(r)

# a=[1, 6, 3, 4, 5]
# b=a[0]
# for i in a:
#     if i>b:
#         b=i
# print(b)

# a=[1,2,{"name":"uday","age":22},[1,2,3,4,5,6],(1,2,3,4,4,5)]
#
# for i in a:
#     if isinstance(i,dict):
#         for x in i:
#             print(x)
#             print(i[x])
#     elif isinstance(i,tuple):
#         for y in i:
#             print(y)
#     elif isinstance(i,list):
#         for z in i:
#             print(z)
#     else:
#         print(i)
#

# a=[1,2,3,4,5]
# b=int(input("enter a number"))
# for i in a:
#     if i in b:
#         a.remove(i)
# print(a)


# b=float(input("enter a number"))
# a.remove(b)
# print(a)

# a = [1, 2, 4, 5]
# b = int(input("Enter a number: "))
#
# # Use a list comprehension to remove the number 'b' from the list 'a'
# a = [i for i in a if i == b]
#
# print(a)

# a=[1,2,4,5]
# a.insert(2,3)
# print(a)
# a.append(3)
# print(a)
# a.sort()
# print(a)


a=[1,2,3,4,5]
b=0

for i in a:
    b+=i
print(b)
