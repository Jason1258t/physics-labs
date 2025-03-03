class ExperimentData:
    def __init__(self, m, times):
        self.m = m
        self.times = times

    def avg_t(self):
        return sum(self.times) / len(self.times)


class GeneralParameters:
    md = 0.1245
    mo = 0.033
    Rd = 0.085 / 2
    Rk = 0.105 / 2
    Ro = 0.01 / 2
    h = 0.4


def f79(params: GeneralParameters, experiment: ExperimentData):
    md = params.md
    Rd = params.Rd
    Ro = params.Ro
    mk = experiment.m
    Rk = params.Rk
    mo = params.mo
    return 0.5 * (md * (Rd ** 2 + Ro ** 2) + mk * (Rk ** 2 + Rd ** 2) + mo * Ro ** 2)


def f712(m, h):
    return m * 9.8 * h


def f714(h, t, m, J, D):
    return (2 * h ** 2 / (t ** 2)) * (m + 4 * J / (D ** 2))


def f76(ex: ExperimentData, params: GeneralParameters):
    m = ex.m + params.md + params.mo
    return m * (params.Ro * 2) ** 2 / 4 * ((9.8 * ex.avg_t() ** 2) / (2 * params.h) - 1)


e1 = ExperimentData(0.552, [2.371, 2.225, 2.332, 2.271, 2.294])
e2 = ExperimentData(0.256, [2.253, 2.227, 2.242, 2.236, 2.243])
e3 = ExperimentData(0.389, [2.334, 2.312, 2.340, 2.332, 2.327])


def match(experiment: ExperimentData):
    params = GeneralParameters()
    J = f79(params, experiment)
    print('J by 7.9: ', J)
    J = f76(experiment, params)
    print('J by 7.6:', J)
    Ep = f712(experiment.m + params.mo + params.md, params.h)
    Ek = f714(params.h, experiment.avg_t(), experiment.m + params.md + params.mo, J, params.Ro * 2)
    print('Ep: ', Ep, 'Ek:', Ek)


match(e1)
match(e2)
match(e3)
