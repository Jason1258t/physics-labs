# r = float(input('Расстояние до маршмеллоу от центра R : '))
r = 0.123
h = 1
d = float(input('Диаметр : '))
m = float(input('Масса m : '))
# h = float(input('Длина пути h : '))
t = list(map(float, input('Тайминги через пробел : ').split()))
t_aver = sum(t)/len(t)

def E(h, t, d):
    e = (4*h)/((t**2) * d)
    return e

def M(m, h, t, d):
    g = 9.8
    M = m*g*(1 - ((2*h)/(g*(t**2))))*(d/2)
    return M

def output():
    print(f'm: {m}')
    print(f'd: {d}')
    print(f'h: {h}')
    print(f't: {' '.join(list(map(str, t)))}')
    print(f't_aver: {t_aver}')
    print(f'R: {r}')
    print(f'E: {E(h, t_aver, d)}')
    print(f'M: {M(m, h, t_aver, d)}')

output()