from datetime import date, timedelta
import pandas as pd
from dateutil.relativedelta import relativedelta, MO



def is_holiday(_date: date) -> bool:
    def transform(df) -> dict:
        df['date'] = [
            '/'.join(dt.split('/')[:-1] + [f'20{dt.split("/")[-1]}'])
            for dt in df['date']
        ]
        print(df['date'])
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        df['date'] = df['date'].dt.strftime('%d-%m-%Y')

        holidays = {}
        for _date, holiday in zip(df['date'], df['holiday']):
            holidays[_date] = holiday
        return holidays

    def get_holidays() -> dict:
        df = pd.read_csv('holidays.csv')
        print(df)
        holidays = transform(df)
        return holidays

    holidays = get_holidays()
    if holidays.get(_date.strftime('%d-%m-%Y'), ''):
        return True
    return False


def is_weekend(_date: date) -> bool:
    return _date.weekday() > 4

def get_next_monday_from_date(_date: date) -> date:
    return _date + relativedelta(weekday=MO(1))

def get_next_day_from_date(_date: date) -> date:
    return _date + timedelta(days=1)

def get_business_date_from(_date: date) -> date:
    if is_weekend(_date):
        next_monday_date: date = get_next_monday_from_date(_date)
        return get_business_date_from(next_monday_date)

    if is_holiday(_date):
        next_day_date: date = get_next_day_from_date(_date)
        return get_business_date_from(next_day_date)

    return _date

_date = date(2025, 3, 1)
print(get_business_date_from(_date))
