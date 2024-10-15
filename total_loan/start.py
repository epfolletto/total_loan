from app import total_loan
from datetime import date

lista_entrada = [
    # p_1 [0]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
        'amortization_system': 'price',
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
    # -------------------------------------------------------------------------
    # s_1 [16]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'amortization_system': 'sac',
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
        'date_0': date(2024, 6, 17),
        'date_1': date(2024, 7, 17)
    },
    # s_2 [17]
    {
        'contract_value': 70_568_447.85,
        'debit_balance': 64_782_442.98,
        'term': 120,
        'annual_rate': 7.99,
        'amortization_system': 'sac',
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
        'date_0': date(2024, 6, 17),
        'date_1': date(2024, 7, 17)
    },
    # s_3 [18]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 420,
        'annual_rate': 7.99,
        'amortization_system': 'sac',
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
    # s_iof_2 [19]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'amortization_system': 'sac',
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
        'date_0': date(2024, 6, 17),
        'date_1': date(2024, 7, 17)
    },
    # s_c_iof_3 [20]
    {
        'contract_value': 400_000,
        'debit_balance': 375_000,
        'term': 120,
        'annual_rate': 7.99,
        'amortization_system': 'sac',
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
        'date_0': date(2024, 6, 17),
        'date_1': date(2024, 8, 28)
    },
    # s_c_iof_4 [21]
    {
        'contract_value': 42_000_000,
        'debit_balance': 31_700_000,
        'term': 120,
        'annual_rate': 7.99,
        'amortization_system': 'sac',
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
        'date_0': date(2024, 9, 7),
        'date_1': date(2024, 12, 27)
    },
    # s_c_iof_5 [22]
    {
        'contract_value': 20_000_000,
        'debit_balance': 17_680_000,
        'term': 120,
        'annual_rate': 7.99,
        'amortization_system': 'sac',
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
        'date_1': date(2024, 12, 27)
    },
    # s_c_iof_6 [23]
    {
        'contract_value': 10_598_146.55,
        'debit_balance': 7_456_823.41,
        'term': 417,
        'annual_rate': 7.99,
        'amortization_system': 'sac',
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
        'legal_nature': 'pj',
        'date_0': date(2024, 12, 2),
        'date_1': date(2024, 12, 23)
    },
    # s_c_iof_7 [24]
    {
        'contract_value': 9_555_321,
        'debit_balance': 6_680_736,
        'term': 360,
        'annual_rate': 7.99,
        'amortization_system': 'sac',
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
        'date_1': date(2024, 10, 30)
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
    # -------------------------------------------------------------------------
    {
    'qitech': 411_041.66, # s_1
    },
    {
    'qitech': 71_083_642.63, # s_2
    },
    {
    'qitech': 411_041.66, # s_3
    },
    {
    'qitech': 425_382.41, # s_iof_2
    },
    {
    'qitech': 425521.57, # s_c_iof_3
    },
    {
    'qitech': 36_413_077.74, # s_c_iof_4
    },
    {
    'qitech': 20_127_348.07, # s_c_iof_5
    },
    {
    'qitech': 8_472_239.51, # s_c_iof_6
    },
    {
    'qitech': 7_715_403.5, # s_c_iof_7
    },
]

# p_i, resumo = total_loan_price(**lista_entrada[9])
# p_i = total_loan(**lista_entrada[19])
#
# print('-------------------------------------')
# print('pi:', p_i)
# print('-------------------------------------')

# for i in resumo:
#     print(i)

count = 0
for i in lista_entrada:
    # p_i, resumo = total_loan_price(**i)
    p_i = total_loan(**i)
    summary[count]['total_loan'] = p_i
    print(count,
          '|',
          i['amortization_system'],
          '|',
          'qitech:', summary[count]['qitech'],
          '|',
          'meu:', f"{p_i:.2f}",
          '|',
          'dif:', f"{summary[count]['qitech'] - p_i:.3f}"
    )
    count += 1