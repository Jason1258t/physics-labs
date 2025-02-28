class ExperimentData:
    def __init__(self, m, times):
        self.m = m
        self.times = times

    def avg_t(self):
        return sum(self.times) / len(self.times)

t1 = ExperimentData(0.552, [2.371, 2.225, 2.332, 2.271, 2.294])

md = 0.1245
mo = 0.033
d = 0.01
h = 0.4

def f(ex: ExperimentData):
    m = ex.m + md + mo
    print(m)
    return m * d ** 2 / 4 * ((9.8 * ex.avg_t() ** 2) / (2 * h) - 1)

print(t1.avg_t())
print(f(t1))