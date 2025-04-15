# a=[]
# for i in range(0,11):
#     a.append(i)
# print(a)
from operator import itemgetter

# a=[1,2,3,5,4,5,6,7,7,9]
# for i in a:
#     if i==4:
#         print(i)
#         break
# else:
#     print("4 is not found")


# a=[3,2,3,4,5,6,7,8,9]
# for i in range(len(a)):
#     print(i)
#     print(a[i])


# a=[1,2,3,4,5,6,7,8,9,10]
# b=(i**2 for i in range(101) if i%2==0)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


# a=[1,2,1,2,3,4,5,6,7]
# b=[]
# for i in a:
#     b.append(i)
# print(list(b))

# my_list=[1,2,[1,2,3],4,[5,6],7]
# for i in my_list:
#     if isinstance(i,list):
#         for ele in i:
#             print(ele)
#     else:
#         print(i)
#
# a={'a':3}
# print(type(a))

# my_list=[1,2,[1,2,3],4,[5,6],7]
# for i in my_list:
#     if type(i)==list:
#         for ele in i:
#             print(ele)
#     else:
#         print(i)

# thisdict =	{"brand": "Ford",{"model": "Mustang", "year": 1964 }}
#
# for i in thisdict:
#     if type(thisdict[i])==dict:
#         for ele in i:
#             print(ele,ele[i])
#
# else:
#     print(i,thisdict[i])


# thisdict = {
#     "brand": "Ford",
#     "details": {"model": "Mustang", "year": 1964}
# }
#
# for key in thisdict:
#     if type(thisdict[key]) == dict:
#         for sub_key in thisdict[key]:
#             print(sub_key, thisdict[key][sub_key])
#     else:
#         print(key, thisdict[key])

a=[1]
b=[2]
a.extend(b)
print(a)

