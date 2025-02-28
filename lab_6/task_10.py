import matplotlib.pyplot as plt

E = list(map(float, input('Значения E через пробел : ').split()))
M = list(map(float, input('Значения M через пробел : ').split()))

plt.plot(E, M, 'ro')
plt.plot(E, M)
plt.show()