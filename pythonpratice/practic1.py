# a=[1,2,3,4,5,6,6,7]
# if a[0]>a[1]:
#     flarge=a[0]
#     slarge=[1]
# else:
#     flarge = a[1]
#     slarge = [0]


#
# for i in range(2,len(a)):
#     if a[i]>flarge:
#         slarge=flarge
#         flarge = a[i]
#
#     elif a[i]>slarge:
#         slarge=a[i]
# print(slarge,flarge)


# a=[8,9,3,4,5,6,7]
# if a[0]>a[1]:
#     flarge=a[0]
#     slarge=a[1]
# else:
#     flarge = a[1]
#     slarge = a[0]
# tlarge = float('-inf')
#
#
# for i in range(2,len(a)):
#     if a[i]>flarge:
#         tlarge = slarge
#         slarge=flarge
#         flarge = a[i]
#
#
#
#     elif a[i]>slarge and a[i]!=flarge:
#         slarge=a[i]
#         tlarge=slarge
#
#     elif a[i]>tlarge and a[i]!=flarge and a[i]!=slarge:
#         tlarge=a[i]
#
# print(flarge,slarge,tlarge)


# a=[1,2,3,4,5,6,7,8,9]
# b=a[0]
#
# for i in a:
#     if i>b:
#         b=i
# print(b)
#

# a=[1,2,3,4,5,6,7,8,9]
# b=a[0]
# for i in a:
#     if b>i:
#         b=i
# print(b)



# a=[1,2,3,4,5,6,7,8,9]
# b=a[0]
# for i in range(len(a)):
#     if a[i]>b:
#         b=a[i]
# print(b)

# a,b=10,20
# a,b=b,a
# print(a,b)

# nested=[1,2,3,[4,5,6],7,8,9]
# for i in nested:
#     if isinstance(i,list):
#         for j in i:
#             print(j)
#

# a=[[1,2],[2,3],[3,4]]
# b=[num for sub in a for num in sub ]
# print(b)
#
#
# a=[1,2,3,4,5,6,7,8,9]
# for i in a:
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 print(i,"not a prime")
#                 break
#         else:
#              print(i,"prime")
#     else:
#         print(i,"purely not a prime")

# a="welcome"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

a=[1,2,3,4,5]
b=0
for i in a:
    b=i+b
print(b)



