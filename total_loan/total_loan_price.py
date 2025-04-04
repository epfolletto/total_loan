def calculate_total_loan_price(days, debit_balance, term, basic_iof,
                             fee_additional_iof, has_iof, fee_volpi, fee_baas,
                             itbi, custas, monthly_rate, nod):

    def calculate_pmt(p):
        return float(p * monthly_rate / (1 - (1 + monthly_rate) ** (-term)))

    def create_flow(p_a, pmt=None):
        pmt_a = pmt or calculate_pmt(p_a)
        days_sum = 0
        iof_t = 0
        iof_basico_t =  0
        iof_adicional_t =  0
        sd_a = p_a
        for i in range(0, term):
            if i == 0:
                j_a = sd_a * (1 + monthly_rate) ** (days[i] / nod) - sd_a
            else:
                j_a = sd_a * (monthly_rate) + extra * (1 + monthly_rate)
            amortiz_a = max(0, pmt_a - j_a)
            sd_a = sd_a - amortiz_a
            days_sum += days[i]
            iof_basico_row = min(365, days_sum) * amortiz_a * basic_iof / 100 if has_iof else 0
            iof_basico_t += iof_basico_row
            iof_adicional_row = amortiz_a * fee_additional_iof / 100 if has_iof else 0
            iof_adicional_t += iof_adicional_row
            iof_t = iof_t + iof_basico_row + iof_adicional_row
            extra = max(0, j_a - pmt_a)

        return iof_adicional_t, iof_basico_t, iof_t, sd_a, pmt_a

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
            iof_adicional, iof_basico, iof, sd, pmt = create_flow(float(p), pmt)
            if sd > 0:
                li = pmt
            else:
                ls = pmt
            converg_sd = abs(sd) < tol_sd
            pmt = (li + ls) / 2

        return iof_adicional, iof_basico, iof, pmt, count


    iteracao = 0
    tol1 = 0.00001
    tol2 = 0.0001
    convergencia_3 = False
    p1 = debit_balance
    pmt = None
    iof_adicional = 0
    iof_basico = 0
    iof = 0
    while not convergencia_3:
        iteracao += 1

        p, sd, tac, count = convergencia_p(p1, tol1, iteracao, pmt)

        if abs(sd) < tol1:
            return p, iof_adicional, iof_basico, iof, fee_volpi*p/100, fee_baas*p/100, itbi, custas, iteracao
            
        iof_adicional, iof_basico, iof, pmt, count = convergencia_sd(p, tol2)
        p2 = debit_balance + itbi + custas + tac + iof

        convergencia_3 = abs(p - p2) < tol1

    return p2, iof_adicional, iof_basico, iof, fee_volpi*p2/100, fee_baas*p2/100, itbi, custas, iteracao