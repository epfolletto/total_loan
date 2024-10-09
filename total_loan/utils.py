from datetime import date, timedelta
from dateutil.relativedelta import relativedelta, MO
import pandas as pd
from holidays import holidays


def get_business_date_from(date_0, date_1, financing_term):
    dates = []
    dates.append(date_0)
    for i in range(1, financing_term + 1):
        date_i = date_1 + relativedelta(months=i-1)
        # (ex.: date_1: 29/01/2025 -> date_i: 28/02/2025, passar pro próximo
        # dia)
        if date_i.day < date_1.day:
            date_i = date_i.replace(day=1) + relativedelta(months=1)

        dt1 = date_i + relativedelta(days=1)
        dt2 = date_i
        while dt1 != dt2:
            dt1 = dt2
            if dt2.weekday() > 4:
                dt2 += relativedelta(weekday=MO(1))

            if ((dt2.day, dt2.month, dt2.year) in holidays or (dt2.day, dt2.month) in holidays):
                dt2 += timedelta(days=1)

        dates.append(dt2)
        # dates.append(dt2.strftime('%d/%m/%Y'))

    number_of_days = {
        1: 31,
        2: 30,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    return dates, number_of_days[date_1.month - 1]
