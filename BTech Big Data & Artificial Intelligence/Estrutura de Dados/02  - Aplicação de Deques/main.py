from collections import deque

#criando um deque (tipo deque)
d = deque()
print(d)

#add elementos
d.append('a')
d.append('b')

print(d)

#add elemento a esquerda do deque
d.appendleft('b')
print(d)

#add diversos elementos na direita do deque
d.extend('cdef')
print(d)

#add diversos elementos na esqueda do deque
d.extendleft('ghij')
print(d)

#add elemento em uma posição especifica
d.insert(5,'k')
print(d)

#removendo elemento na direita do deque
d.pop()
print(d)

#removendo elemento na esqueda do deque
d.popleft()
print(d)

#removendo elemento especifico
d.remove('b')
print(d)

#inverter o deque inteiro
d.reverse()
print(d)

#inverter o daque novamente
d.rotate()
print(d)

#limpa todo deque
d.clear()
print(d)

#criar um deque com limite de elementos
d2 = deque(maxlen=20)
print(d2)