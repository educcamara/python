print('Digite a primeira matriz em forma de lista de listas:')
m1 = eval(input(' > '))
print('Digite a segunda matriz em forma de lista de listas:')
m2 = eval(input(' > ')) 

matriz3 = []

for i in range(len(m1)):
    matriz3.append([])
    for k in range(len(m2[0])):
        elem = 0
        for j in range(len(m2)):
            elem += (m1[i][j] * m2[j][k])
            # print(f'a{i+1}{j+1} b{j+1}{k+1}')
        matriz3[i].append(elem)

print('A multiplicação das duas matrizes resultou em:')
print(matriz3)

# exemplo: [[1,2],[2,1]]   [[1,0],[0,1]]