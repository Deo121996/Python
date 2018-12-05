
from pkg1 import *
for i in range(1,10):
    print(i)

a = [1,2,3,4,5]
# count = 0
print("LIST")


for i in range(1,10,2):
    print(i)
    # a[i] = 100
else:
    print("AFTER FOR")
i = 0 
while i<=10:
    i+=1
    b = 10
    
    if i%2 == 0:
        continue
    else:
        print(i)
        print("Print LOOP")
else:
    print("ELSE WHILE")
    print(b)
    
print("AFTER ELSE")
print(b)


temp = ('ashish','manoj','jagdeesh','rahul')
result = ()
# for i in temp:
#     result.append(i[0])

result = tuple([i[0] for i in temp if i == 'ashish'])
print("RESULT")
print(result)

# result = ['a','m','j','r']


# print("LIST")

# print(a)
# setA = {1,2,3,4,5}
# print("SETA")
# for i in setA:
#     print(i)




# dictA = {
#     'a':1,
#     'b':2,
#     'c':3
# }

# print(" DICTIONARY")

# for key, val in dictA.items():
#     print(key, val)

