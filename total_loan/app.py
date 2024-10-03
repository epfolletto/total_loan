from utils_2 import get_business_date_from2
from utils import get_business_date_from
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd


# ---
P = 4

contract_value = 400_000
debit_balance = 375_000
financing_term = 120

annual_interest_rate = 7.5
monthly_interest_rate = (1+annual_interest_rate/100)**(1/12)-1
fee_itbi = 3
fee_costs = 1.9
fee_volpi = 3.25
fee_baas = 0.75
has_iof = True

P1 = debit_balance
pmt = P1 * monthly_interest_rate / (1 - (1 + monthly_interest_rate)**(-financing_term))

date_0 = date(2024, 9, 9)
date_1 = date(2024, 10, 9)

dates = get_business_date_from(date_1)
df = pd.DataFrame(dates, columns=['date'])
df['date'] = pd.to_datetime(df['date'])
df['days'] = (df['date'] - df['date'].shift(1)).dt.days

print(df)