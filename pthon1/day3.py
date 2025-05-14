a= [(1,9,86,90)]

for i in a:
    if type(i)==dict:
        for z in i:
            print(z)
            print(i[z])
    elif isinstance(i,tuple):
            for x in i:
                print(x)

    else:
        print(i)


