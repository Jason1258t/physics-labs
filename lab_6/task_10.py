import matplotlib.pyplot as plt

E = list(map(float, input('Значения E через пробел : ').split()))
M = list(map(float, input('Значения M через пробел : ').split()))

plt.ylabel('значения E')
plt.xlabel('значения M')

plt.plot(M, E, 'ro')
plt.plot(M, E)
plt.show()