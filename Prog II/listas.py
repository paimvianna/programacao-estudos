x = [0,1,2,3,4]
x.append(5)

y = [3,4,5]

print(type(x))
print(x)

print(x+y)
print(x[-1])

print(x[0])
print(x[1])
print(x[2])
print(x[3])
print("------")
print(len(x))
for i in range(0,len(x)):
    print(x[i])

print("------")
for i in x:
    print(i)

print("------")
matriz = []
matriz.append([0,1,2,3])
matriz.append([0,1,2,3,4,5])
matriz.append([0,1,2])

print(matriz)
print(matriz[0])
print(matriz[0][1])