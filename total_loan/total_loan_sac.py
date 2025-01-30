import math


def calculate_total_loan_sac(days, debit_balance, term, basic_iof,
                             fee_additional_iof, has_iof, fee_volpi, fee_baas,
                             itbi, custas):
    def create_flow(p):
        days_sum = 0
        iof_t = 0
        iof_basico_t =  0
        iof_adicional_t =  0
        coef_amort = math.trunc((1/term) * 10**6) / 10**6
        for i in range(0, term):
            if i == term - 1:
                amortiz = (1 - (term - 1) * coef_amort) * p
            else:
                amortiz = coef_amort * p

            days_sum += days[i]
            iof_basico_row = min(365, days_sum) * amortiz * basic_iof / 100 if has_iof else 0
            iof_basico_t += iof_basico_row
            iof_adicional_row = amortiz * fee_additional_iof / 100 if has_iof else 0
            iof_adicional_t += iof_adicional_row
            iof_t = iof_t + iof_basico_row + iof_adicional_row

        return iof_adicional_t, iof_basico_t, iof_t

    def convergencia_p():
        tol1 = 0.0001
        converg_p = False
        count = 0
        p1 = debit_balance
        while not converg_p:
            count += 1

            iof_adicional, iof_basico, iof2 = create_flow(float(p1))

            tac = (fee_volpi / 100 + fee_baas / 100) * p1
            p2 = debit_balance + itbi + custas + tac + iof2
            
            converg_p = abs(p1 - p2) < tol1
            if p1 < p2:
                p1 += abs(p2 - p1)
            else:
                p1 -= abs(p2 - p1)

        return p1, iof_adicional, iof_basico, iof2, fee_volpi*p1/100, fee_baas*p1/100, itbi, custas, count


    return convergencia_p()