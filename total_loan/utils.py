import pandas as pd
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta, MO


def get_business_date_from(date_1):
    df = pd.read_csv('holidays.csv', usecols=['date'],
                     dtype={'date': 'object'}, dayfirst=True)
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
    holidays = df['date'].dt.date.values

    dates = []
    for i in range(1, 120 + 1):
        date_i = date_1 + relativedelta(months=i-1)

        date_check1 = date_i + relativedelta(days=1)
        date_check2 = date_i
        while date_check1 != date_check2:
            date_check1 = date_check2
            if date_check2.weekday() > 4:
                date_check2 += relativedelta(weekday=MO(1))

            if date_check2 in holidays:
                date_check2 += timedelta(days=1)

        dates.append(date_check2)
        # dates.append(date_check2.strftime('%d/%m/%Y'))

    return dates
