from total_loan.total_loan_sac import calculate_total_loan_sac
from total_loan.total_loan_price import calculate_total_loan_price
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

    if amortization_system == 'price':
        p = calculate_total_loan_price(days, debit_balance, term, basic_iof,
                                 fee_additional_iof, has_iof, fee_volpi,
                                 fee_baas, itbi, custas, monthly_rate, nod)

        return p
