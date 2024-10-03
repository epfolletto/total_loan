import pandas as pd
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta, MO


def get_business_date_from(date_0, date_1, financing_term):
    holidays = {
        (1, 1),  # Confraternização Universal
        (26, 2),  # Carnaval
        (27, 2),  # Carnaval
        (13, 4),  # Paixão de Cristo
        (21, 4),  # Tiradentes
        (1, 5),  # Dia do Trabalho
        (14, 6),  # Corpus Christi
        (7, 9),  # Independência do Brasil
        (12 ,10),  # Nossa Sra Aparecida - Padroeira do Brasil
        (2 ,11),  # Finados
        (15 ,11),  # Proclamação da República
        (25 ,12),  # Natal
    }

    dates = []
    dates.append(date_0)
    for i in range(1, financing_term + 1):
        date_i = date_1 + relativedelta(months=i-1)

        date_check1 = date_i + relativedelta(days=1)
        date_check2 = date_i
        while date_check1 != date_check2:
            date_check1 = date_check2
            if date_check2.weekday() > 4:
                date_check2 += relativedelta(weekday=MO(1))

            if (date_check2.month, date_check2.day) in holidays:
                date_check2 += timedelta(days=1)

        dates.append(date_check2)
        # dates.append(date_check2.strftime('%d/%m/%Y'))

    return dates
