from utils_2 import get_business_date_from2
from utils import get_business_date_from
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta


# ---
P = 4

contract_value = 400_000
debit_balance = 375_000
financing_term = 120

annual_interest_rate = 7.5
fee_itbi = 3
fee_costs = 1.9
fee_volpi = 3.25
fee_baas = 0.75

date_0 = date(2024, 9, 9)
date_1 = date(2024, 1, 1)

_date = date_1
for i in range(1, financing_term+1):
    date_i = get_business_date_from2(_date)
    _date = _date + relativedelta(months=1)
    print(date_i)

print('===============================================================')
print('===============================================================')
print('===============================================================')

bla = get_business_date_from(date_1)
for i in bla:
    print(i)
