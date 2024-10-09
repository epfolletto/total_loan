from app import total_loan_price
from datetime import date

lista_entrada = [
    # p_1 [0]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': False,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 9, 9),
        'date_1': date(2024, 10, 9)
    },
    # p_2 [1]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': False,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 9, 12),
        'date_1': date(2024, 10, 14)
    },
    # p_3 [2]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': False,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 9, 12),
        'date_1': date(2024, 10, 14)
    },
    # p_4 [3]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': False,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 9, 9),
        'date_1': date(2024, 12, 9)
    },
    # p_5 [4]
    {
        'contract_value': 30_000_000,
        'debit_balance': 24_500_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': False,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 9, 17),
        'date_1': date(2024, 2, 5)
    },
    # p_6 [5]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 420,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': False,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 9, 9),
        'date_1': date(2024, 10, 9)
    },
    # p_iof_1 [6]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 4, 20),
        'date_1': date(2024, 5, 20)
    },
    # p_iof_2 [7]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 5, 15),
        'date_1': date(2024, 5, 20)
    },
    # p_c_iof_3 [8]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 7, 20),
        'date_1': date(2024, 9, 20)
    },
    # p_c_iof_4 [9]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 5, 6),
        'date_1': date(2024, 7, 29)
    },
    # p_c_iof_5 [10]
    {
        'contract_value': 20_000_000,
        'debit_balance': 16_000_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 5, 6),
        'date_1': date(2024, 7, 29)
    },
    # p_c_iof_6 [11]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 9, 9),
        'date_1': date(2024, 12, 30)
    },
    # p_c_iof_7 [12]
    {
        'contract_value': 60_000_000,
        'debit_balance': 55_590_000,
        'term': 240,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 9, 9),
        'date_1': date(2024, 12, 30)
    },
    # p_c_iof_8 [13]
    {
        'contract_value': 24_900_000,
        'debit_balance': 17_846_000,
        'term': 360,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 8, 30),
        'date_1': date(2024, 11, 21)
    },
    # p_c_iof_9 [14]
    {
        'contract_value': 100_000,
        'debit_balance': 80_000,
        'term': 36,
        'annual_rate': 7.99,
        'has_itbi': True,
        'has_costs': True,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 3.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pf',
        'date_0': date(2024, 7, 31),
        'date_1': date(2024, 10, 21)
    },
    # p_c_iof_10 (nati) [15]
    {
        'contract_value': 11_438_120.42,
        'debit_balance': 7_900_000,
        'term': 300,
        'annual_rate': 12.5,
        'has_itbi': False,
        'has_costs': False,
        'has_iof': True,
        'fee_itbi': 3,
        'fee_costs': 1.9,
        'fee_volpi': 5.25,
        'fee_baas': 0.75,
        'fee_additional_iof': .38,
        'fee_basic_daily_iof_pf': .0082,
        'fee_basic_daily_iof_pj': .0041,
        'legal_nature': 'pj',
        'date_0': date(2024, 9, 30),
        'date_1': date(2024, 11, 21)
    },
]

summary = [
    {
    'qitech': 411041.66, # p_1
    },
    {
    'qitech': 411041.66, # p_2
    },
    {
    'qitech': 411041.66, # p_3
    },
    {
    'qitech': 411041.66, # p_4
    },
    {
    'qitech': 27052083.33, # p_5
    },
    {
    'qitech': 411041.66, # p_6
    },
    {
    'qitech': 425582.29, # p_iof_1
    },
    {
    'qitech': 425448.28, # p_iof_2
    },
    {
    'qitech': 425725.11, # p_c_iof_3
    },
    {
    'qitech': 425817.96, # p_c_iof_3
    },
    {
    'qitech': 18323337.94, # p_c_iof_3
    },
    {
    'qitech': 425900.17, # p_c_iof_3
    },
    {
    'qitech': 63188919.0, # p_c_iof_3
    },
    {
    'qitech': 20583739.08, # p_c_iof_3
    },
    {
    'qitech': 91382.84, # p_c_iof_3
    },
    {
    'qitech': 8575770.56, # p_c_iof_10 (nati)
    },
]

# p_i, resumo = total_loan_price(**lista_entrada[9])
# p_i = total_loan_price(**lista_entrada[0])
#
# print('-------------------------------------')
# print('pi:', p_i)
# print('-------------------------------------')

# for i in resumo:
#     print(i)

count = 0
for i in lista_entrada:
    # p_i, resumo = total_loan_price(**i)
    p_i = total_loan_price(**i)
    summary[count]['total_loan'] = p_i
    print(count, summary[count]['qitech'], '|', p_i, 'dif:', summary[count][
        'qitech'] - p_i)
    count += 1
