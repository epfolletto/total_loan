from utils_2 import get_business_date_from2
from utils import get_business_date_from
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd


# ---

contract_value = 24_900_000
debit_balance = 17_846_000
financing_term = 360

annual_interest_rate = 7.99
monthly_interest_rate = (1+annual_interest_rate/100)**(1/12)-1
fee_itbi = 3
fee_costs = 1.9
fee_volpi = 3.25
fee_baas = 0.75
has_iof = True
fee_additional_iof =0.38
fee_basic_daily_iof_pf =0.0082
fee_basic_daily_iof_pj =0.0041
legal_nature = 'pf'
if legal_nature == 'pf':
    basic_iof = fee_basic_daily_iof_pf
else:
    basic_iof = fee_basic_daily_iof_pj

P1 = debit_balance
def calculate_pmt(p):
    return p * monthly_interest_rate / (1 - (1 + monthly_interest_rate)**(-financing_term))

date_0 = date(2024, 8, 30)
date_1 = date(2024, 11, 21)

dates = get_business_date_from(date_0, date_1, financing_term)
df_i = pd.DataFrame(dates, columns=['date'])
df_i['date'] = pd.to_datetime(df_i['date'])
df_i['days'] = (df_i['date'] - df_i['date'].shift(1)).dt.days
df_i['pmt'] = None
df_i['juros'] = None
df_i['amortizacao'] = None

def variation_of_p(df, p):
    pmt = calculate_pmt(p)
    for i in range(0, financing_term + 1):
        if i == 0:
            df['saldo_devedor'] = p
        else:
            df.at[i, 'pmt'] = pmt
            if i == 1:
                df.at[i, 'juros'] = df.at[i - 1, 'saldo_devedor'] * (1 + monthly_interest_rate) ** (df.at[i, 'days'] / 31) - df.at[i - 1, 'saldo_devedor']
            else:
                df.at[i, 'juros'] = df.at[i - 1, 'saldo_devedor'] * monthly_interest_rate + df.at[i - 1, 'extra'] * (1 + monthly_interest_rate)
            if df.at[i, 'juros'] > df.at[i, 'pmt']:
                df.at[i, 'amortizacao'] = 0
            else:
                df.at[i, 'amortizacao'] = df.at[i, 'pmt'] - df.at[i, 'juros']
            df.at[i, 'saldo_devedor'] = (df.at[i - 1, 'saldo_devedor'] - df.at[i, 'amortizacao'])
            if i == 1:
                df.at[i, 'days_iof'] = df.at[i, 'days']
            else:
                df.at[i, 'days_iof'] = min(df.at[i - 1, 'days_iof'] + df.at[i, 'days'], 365)
            df.at[i, 'iof_basico'] = (basic_iof / 100) * df.at[i, 'amortizacao'] * df.at[i, 'days_iof']
            df.at[i, 'iof_adicional'] = (fee_additional_iof / 100) * df.at[i, 'amortizacao']
            df.at[i, 'iof_total'] = df.at[i, 'iof_basico'] + df.at[i, 'iof_adicional']
            if df.at[i, 'juros'] < df.at[i, 'pmt']:
                df.at[i, 'extra'] = 0
            else:
                df.at[i, 'extra'] = df.at[i, 'juros'] - df.at[i, 'pmt']

    return df

print(variation_of_p(df_i, 24_900_000))

# for index, row in df.iterrows():
#     print({row['date']})