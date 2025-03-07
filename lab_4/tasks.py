import math

# m = float(input('Введите массы m1, m2 : ').split())
# l = float(input('Введите длину подвеса шаров l : '))
# a = float(input('Введите угол a : '))
# a_list = [(tuple(input('Введите a1, a2 через пробел : ').split())) for i in range(5)]
# dt = float(input('Введите dt : '))
m = float()
l = float()
a = float()
a_list = [(), (), (), (), ()]
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

def task1():
    global m, l, a, a_list, dt, g
    v1 = V(a)
    res = []
    for i in a_list:
        u1, u2 = U(i[0]), U(i[1])
        res.append({
            'u1': u1,
            'u2': u2,
        })
    print(f'v1 : {v1}')
    for i in range(len(a_list)):
        data = res[i]
        print(f'u1 : {data['u1']}\nu2 : {data['u2']}\n')
    a1_aver = sum([i[0] for i in a_list])/len(a_list)
    a2_aver = sum([i[1] for i in a_list])/len(a_list)
    u1, u2 = U(a1_aver), U(a2_aver)
    kv = Kv(u1, u2, v1)
    ke = Ke(u1, u2, v1)
    print(f'Kv : {kv}\nKe : {ke}')

def Wod(m, u1, u2, v1):
    wod = ((m * v1**2)/2 - (m * u1**2)/2 - (m * u2**2)/2) / 2
    return wod

def task2():
    global m, a_list, a
    v1 = V(a)
    res = []
    for i in a_list:
        u1, u2 = U(i[0]), U(i[1])
        wod = Wod(m, u1, u2, v1)
        res.append({
            'wod': wod,
        })
    print(*[f'Wod : {i['wod']}' for i in res], sep='\n')

def task3():
    pass
