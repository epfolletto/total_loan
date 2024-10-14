import math


def calculate_total_loan_sac(days, debit_balance, term, basic_iof,
                             fee_additional_iof, has_iof, fee_volpi, fee_baas,
                             itbi, custas):
    def create_flow(p):
        days_sum = 0
        iof_t = 0
        coef_amort = math.trunc((1/term) * 10**6) / 10**6
        for i in range(0, term):
            if i == term - 1:
                amortiz = (1 - (term - 1) * coef_amort) * p
            else:
                amortiz = coef_amort * p

            days_sum += days[i]
            iof_b = min(365, days_sum) * amortiz * basic_iof / 100
            iof_a = amortiz * fee_additional_iof / 100
            iof_t += (iof_b + iof_a) if has_iof else 0

        return iof_t

    def convergencia_p():
        tol1 = 0.001
        converg_p = False
        count = 0
        p1 = debit_balance
        while not converg_p:
            count += 1

            iof2 = create_flow(float(p1))

            tac = (fee_volpi / 100 + fee_baas / 100) * p1
            p2 = debit_balance + itbi + custas + tac + iof2

            converg_p = abs(p1 - p2) < tol1
            if p1 < p2:
                p1 += abs(p2 - p1)
            else:
                p1 -= abs(p2 - p1)

        return p1


    return convergencia_p()