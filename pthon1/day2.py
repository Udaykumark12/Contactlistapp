# # a="Hello world"
# # b="aeiou"
# # c=[]
# # for i in a:
# #     if i in b:
# #        c.append(i)
# #
# # print(c)

#
# a="hello "
# b="oelorko"
# c=[]
# for i in b:
#     if i in a:
#         c.append(i)
# print(c)
#
# a="hello world"
# c={}
# for i in a:
#     if i in c:
#         c[i]+=1
#     else:
#         c[i]=1
# print(c)


# a={'a':"uday",'b':"nirmal",'c':"rakju"}
# print(a["a"])


# def a(marks):
#     if marks>=35:
#          return True
#     else:
#        return False
# x=[88,3,44,55,66]
# z=filter(a,x)
# print(list(z))

# a="qqqqqqqqqqqqqqqqqqqqqqqqqqqq"
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)


#
# data = [
# [1, 2, 3],
# {"name": "John", "age": 30},
# [4, 5, 6],
# {"city": "New York", "country": "USA"},
# [7, 8, 9],
# {"occupation": "Engineer", "salary": 50000}
#
# ]
#
# # print(data[5]["occupation"],data[5]["salary"])
# # print(data[3]['city'])
# # print(data[4][2])
# print(data[1]["age"])



# my_dict={
#    "username" : "my_username",
#    "password" : "my_password",
#    "validation-factors" : {
#       "validationFactors" : [
#          {
#             "name" : "remote_address",
#             "value" : "127.0.0.1"
#          }
#       ]
#    }
# }
#
# print(my_dict['validation-factors']["validationFactors"][0]["name"])



class A:
    def m(self):
        self.a=4
        self.b=4
        # print(self.a+self.b)

    def n(self):
        self.m()
        print(self.a+self.b)

c=A()
c.n()