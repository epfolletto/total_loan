from total_loan.total_loan_sac import calculate_total_loan_sac
from utils import get_business_date_from

def total_loan(**dados):
    contract_value = dados.get('contract_value')
    debit_balance = dados.get('debit_balance')
    term = dados.get('term')
    annual_rate = dados.get('annual_rate')
    amortization_system = dados.get('amortization_system')
    has_itbi = dados.get('has_itbi')
    has_costs = dados.get('has_costs')
    has_iof = dados.get('has_iof')
    fee_itbi = dados.get('fee_itbi')
    fee_costs = dados.get('fee_costs')
    fee_volpi = dados.get('fee_volpi')
    fee_baas = dados.get('fee_baas')
    fee_additional_iof = dados.get('fee_additional_iof')
    fee_basic_daily_iof_pf = dados.get('fee_basic_daily_iof_pf')
    fee_basic_daily_iof_pj = dados.get('fee_basic_daily_iof_pj')
    legal_nature = dados.get('legal_nature')
    date_0 = dados.get('date_0')
    date_1 = dados.get('date_1')

    # pre-processamento
    if legal_nature == 'pf':
        basic_iof = fee_basic_daily_iof_pf
    else:
        basic_iof = fee_basic_daily_iof_pj
    itbi = (fee_itbi / 100) * contract_value if has_itbi else 0
    custas = (fee_costs / 100) * contract_value if has_costs else 300
    monthly_rate = (1 + annual_rate / 100) ** (1/12)-1

    dates, nod = get_business_date_from(date_0, date_1, term)

    days = []
    for i in range(1, len(dates)):
        days.append((dates[i]-dates[i-1]).days)

    if amortization_system == 'sac':
        p = calculate_total_loan_sac(days, debit_balance, term, basic_iof,
                                 fee_additional_iof, has_iof, fee_volpi,
                                 fee_baas, itbi, custas)

        return p


    def calculate_pmt(p):
        return float(p * monthly_rate / (1 - (1 + monthly_rate) ** (-term)))

    def create_flow(p_a, pmt=None):
        pmt_a = pmt or calculate_pmt(p_a)
        days_sum = 0
        iof_t = 0
        sd_a = p_a
        for i in range(0, term):
            if i == 0:
                j_a = sd_a * (1 + monthly_rate) ** (days[i] / nod) - sd_a
            else:
                j_a = sd_a * (monthly_rate) + extra * (1 + monthly_rate)
            amortiz_a = max(0, pmt_a - j_a)
            sd_a = sd_a - amortiz_a
            days_sum += days[i]
            iof_b = min(365, days_sum) * amortiz_a * basic_iof / 100
            iof_a = amortiz_a * fee_additional_iof / 100
            iof_t += (iof_b + iof_a) if has_iof else 0
            extra = max(0, j_a - pmt_a)

        return iof_t, sd_a, pmt_a

    def convergencia_p(p1, tol1, iteracao, pmt=None):
        converg_p = False
        count = 0
        while not converg_p:
            count += 1
            if iteracao == 1:
                iof2, sd, pmt = create_flow(float(p1))
            else:
                iof2, sd, pmt = create_flow(float(p1), pmt)

            tac = (fee_volpi / 100 + fee_baas / 100) * p1
            p2 = debit_balance + itbi + custas + tac + iof2
            converg_p = abs(p1 - p2) < tol1
            if p1 < p2:
                p1 += abs(p2 - p1)
            else:
                p1 -= abs(p2 - p1)

        return p1, sd, tac, count

    def convergencia_sd(p, tol_sd):
        converg_sd = False
        ls = debit_balance
        li = 0
        pmt = (li + ls) / 2
        count = 0
        while not converg_sd:
            count += 1
            iof, sd, pmt = create_flow(float(p), pmt)
            if sd > 0:
                li = pmt
            else:
                ls = pmt
            converg_sd = abs(sd) < tol_sd
            pmt = (li + ls) / 2

        return iof, pmt, count


    iteracao = 0
    tol1 = 0.001
    tol2 = 0.001
    convergencia_3 = False
    resumo = []
    p1 = debit_balance
    pmt = None
    while not convergencia_3:
        iteracao += 1

        p, sd, tac, count = convergencia_p(p1, tol1, iteracao, pmt)

        if abs(sd) < tol1:
            return p

        iof, pmt, count = convergencia_sd(p, tol2)
        p2 = debit_balance + itbi + custas + tac + iof

        convergencia_3 = abs(p - p2) < tol1

    return p2

