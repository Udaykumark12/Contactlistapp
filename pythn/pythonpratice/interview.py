# a=[1,2,3,[4,5,6],2,3,4]
#
# for i in a:
#     if type(i)==list:
#         for ele in i:
#             print(ele)
#     else:
#         print(i)
from itertools import count

# a=[1,2,3,[4,5,6],7,8,9]
# for i in a:
#     if isinstance(i,list):
#         for ele in i:
#             print(ele)
#     else:
#         print(i)

# a = {
#     "Name": "uday",
#     "Details": {"age": 24, "place": "kippam"}
# }
#
# for i in a:
#     if isinstance(a[i], dict):
#         for ele in a[i]:
#             print(ele, a[i][ele])
#     else:
#         print(i, a[i])



# a = [{
#     "Name": "uday",
#     "Details": {"age": 24, "place": "kuppam"}
# },(1,2,3,4)]
#
# for i in a:
#     if isinstance(i, int):
#         for ele in i:
#             print(ele)
#     elif isinstance(a[i], dict):
#         for key in a[i]:
#             print(key.a[i][key])
#     else:
#         print(i, a[i])

# a = [{
#     "Name": "uday",
#     "Details": {"age": 24, "place": "kuppam"}
# }, (1, 2, 3, 4)]
#
# for i in a:
#     if isinstance(i, int) or isinstance(i, tuple):
#         for x in i:
#             print(x)
#     elif isinstance(i, dict):
#         for key in i:
#             print(key, i[key])
#             if isinstance(i[key], dict):  # Check if the value is a dictionary
#                 for sub_key in i[key]:
#                     print( sub_key ,i[key][sub_key])  # Indented for clarity
#     else:
#         print(i)


#
# dict1 = [{
#     "Name": "uday",
#     "Details": {"age": 24, "place": "kuppam"}
# }, (1, 2, 3, 4)]
#
# for mydict in dict1:
#     if isinstance(mydict,int) or isinstance(mydict,tuple):
#         for list in mydict:
#             print(list)
#
#     elif isinstance(mydict,dict):
#         for newdict in mydict:
#             print(newdict)
#             if isinstance(mydict[newdict],dict):
#                 for subdict in mydict[newdict]:
#                     print(subdict,mydict[newdict][subdict])



#
# a=[{"Name":"uday",
#    "age":{"height":24}
#
#    }]
#
# for i in a:
#     if isinstance(i,dict):
#         for x in i:
#             print(x,i[x])
#             if isinstance(i[x],dict):
#                 for z in i[x]:
#                     print(z,i[x][z])
#     else:
#         print(i)
#
# def age(num):
#     if num<0:
#         raise ValueError("only integers")
#     if num%2==0:
#         print("even")
#
#     else:
#         print("exception not occured")
#
#
# try:
#     num = int(input("Enter a number: "))
#     age(num)
# except:
#     print("Exception occurred:")


#
# a=[{"Name":"uday",
#    "age":{"height":24}
#
#    }]
#
# for i in a:
#     if isinstance(i,dict):
#         for x in i:
#             print(x,i[x])
#
#     if isinstance(i[x],dict):
#         for y in i[x]:
#             print(y,i[x][y])

#
# a=["A","B",'c','d','e','f','g']
# # [ 0,  1, 2,  3,  4,  5,   6,  7]
# for i in range(len(a)-2,len(a)):
#     print(i)
#     # print(len(a),"uday")
# print(len(a))


# employees = {"satyam": [35, 50000],
#
#              "shivam": [45, 60000],
#
#              "Bhaskar": [55, 70000]
#
#              }

#approach1

# vals = employees.values()
# vals = [i[1] for i in vals]
# print(vals)
# lowest = min(vals)
# print(lowest)
#
# #approach2
#
# for k, v in employees.items():
#     if lowest in v:
#         print(k, lowest)


# Output: satyam
# Find the employee name & his age whose salary is lowest.


# Convert a nested list into a simple list.
# input = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]
#
# # output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
#
# l = []
#
#
# def fun_nested_list(l1):
#     for i in l1:
#         if isinstance(i, list):
#             fun_nested_list(i)
#         else:
#             l.append(i)
#     return l
#
#
# print(fun_nested_list(input))



#dictionary count



# d = {"name": "sai", "place": "bang", "interview": "msys", 1: "sai", 2: "bang", 3: "bang", 4: "msys"}
#
# c = {}
# for key, value in d.items():
#     if value in c:
#         c[value] += 1
#     else:
#         c[value] = 1
#
# print(c)

# d = {"name": "sai", "place": "bang", "interview": "msys", 1: "sai", 2: "bang", 3: "bang", 4: "msys"}
#
# for key, value in d.items():
#     if key:"name":
#         print(value)


# a="hello world"
# c={}
# for i in a:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1
# print(c)


# a="hello world"
# result=a.split()
# print(result)
# for i in result:
#     print(i[::-1])

#
# a=[1,2,3,4,5]
# b=a[0]
# for i in a:
#     if i>b:
#         b=i
# print(b)

# a = "udayudayuudayday"
# v = "aeiou"
# c = []
#
# for i in a:
#     if v.count(i) > 1:
#         c.append(i)
#
# print(c)

# a = "udayudayuudayday"
# v = "udayudayuday"
# c = []
#
# for i in a:
#     if i not in c and v.count(i)>1:
#         c.append(i)
# print(c)

# a = "udayudayuudayday"
# v = "aeiou"
# c = []
#
# for i in v:
#     if a.count(i)>1:
#         c.append(i)
# print(c)


a = "abcdefgh"
v = "abcdefghab"
c = []

for i in a:
    if v.count(i)>1:
        c.append(i)
print(c)


