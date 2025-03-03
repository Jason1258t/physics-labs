e = float(input('E: '))
h = 1
t = list(map(float, input('Тайминги через пробел : ').split()))
d = float(input('d: '))
dh = 0.005
dt = (max(t) - min(t)) / 2
dd = 0.05 / 1000
t_avg = sum(t) / len(t)
print('de:', ((dh / h) + 2 * (dt / t_avg) + (dd / d)) * e)
