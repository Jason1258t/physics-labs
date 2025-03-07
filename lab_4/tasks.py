import math

# m = float(input('Введите массы m1, m2 : ').split())
# l = float(input('Введите длину подвеса шаров l : '))
# a = float(input('Введите угол a : '))
# a_list = [(tuple(input('Введите a1, a2 через пробел : ').split())) for i in range(5)]
# dt = float(input('Введите dt : '))
m = 0.1122
l = 0.33
a = 15.0
a_list = [(3.0, 11.5), (3.5, 11.75), (3.25, 11.75), (2.75, 12.0), (3.25, 11.75), (3.15, 11.75)]
dt = float()
g = 9.8

def U(a):
    u = 2 * math.sqrt(g*l) * math.sin(math.radians(a/2))
    return u

def V(a):
    v = 2 * math.sqrt(g*l) * math.sin(math.radians(a/2))
    return v

def Kv(u1, u2, v1):
    kv = abs(u1 - u2) / abs(v1)
    return kv

def Ke(u1, u2, v1):
    ke = (u1**2 + u2**2) / (v1**2)
    return ke

a1_aver, a2_aver = 0, 0
def task1(out=True):
    global m, l, a, a_list, dt, g, a1_aver, a2_aver
    v1 = V(a)
    a1_aver = sum([i[0] for i in a_list])/len(a_list)
    a2_aver = sum([i[1] for i in a_list])/len(a_list)
    u1, u2 = U(a1_aver), U(a2_aver)
    kv = Kv(u1, u2, v1)
    ke = Ke(u1, u2, v1)
    if out:
        print(f'v1 : {v1}\nu1 : {u1}\nu2 : {u2}\nKv : {kv}\nKe : {ke}')

def Wod(m, u1, u2, v1):
    wod = ((m * v1**2)/2 - (m * u1**2)/2 - (m * u2**2)/2) / 2
    return wod

def task2():
    global m, a_list, a, a1_aver, a2_aver
    v1 = V(a)
    u1, u2 = U(a1_aver), U(a2_aver)
    wod = Wod(m, u1, u2, v1)
    print(f'Wod : {wod}')

def task3():
    pass

task1(0)
task2()