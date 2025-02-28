def f79(md, Rd, Ro, mk, Rk, mo):
    return 0.5 * (md * (Rd ** 2 + Ro ** 2) + mk * (Rk ** 2 + Rd ** 2) + mo * Ro ** 2)

def f712(m, h):
    return m * 9.8 * h

def f714(h, t, m, J, D):
    return (2 * h ** 2 / (t ** 2)) * (m + 4 * J / (D ** 2))


class ExperimentData:
    def __init__(self, m, times):
        self.m = m
        self.times = times

    def avg_t(self):
        return sum(self.times) / len(self.times)

md = 0.1245
mo = 0.033
Rd = 0.085 / 2
Rk = 0.105 / 2
Ro = 0.01 / 2
h = 0.4

e1 = ExperimentData(0.552, [2.371, 2.225, 2.332, 2.271, 2.294])
e2 = ExperimentData(0.256, [2.253, 2.227, 2.242, 2.236, 2.243])
e3 = ExperimentData(0.389, [2.334, 2.312, 2.340, 2.332, 2.327])

def match(experiment: ExperimentData):
    J = f79(md, Rd, Ro, experiment.m, Rk, mo)
    print('J: ', J)
    Ep = f712(experiment.m + md + mo, h)
    Ek = f714(h, experiment.avg_t(), experiment.m + md + mo, J, Ro * 2)
    print('Ep: ', Ep, 'Ek:', Ek)

match(e1)
match(e2)
match(e3)