import pandas as pd
import numpy as np
import random
import math
from datetime import date, timedelta
# from client_generator import client_generator

def loan_generator(clients):
    rng = np.random.default_rng(42)

    possible_loan_quantity = np.arange(1, 11)
    weights = .5 ** possible_loan_quantity
    weights /= weights.sum()

    loan_quantity_array = rng.choice(possible_loan_quantity, size=50_000, p=weights)
    total_loan_quantity = loan_quantity_array.sum()

    loan_id_array = rng.choice(np.arange(1_000, 10_000_001), size=total_loan_quantity, replace=False)
    
    log_min = math.log(1_000)
    log_max = math.log(10_000_000)
    random.seed(42)

    loan_amount_array = [
        round(math.exp(random.uniform(log_min, log_max)), -2)
        for _ in range(total_loan_quantity)
    ]

    years = list(range(2015, 2026))
    weights = [y - 2015 + 1 for y in years]

    dates_by_year = {}
    for y in years:
        start = date(y, 1, 1)
        end = date(y, 12, 31)
        dates_by_year[y] = [
            start + timedelta(days=i)
            for i in range((end - start).days + 1)
        ]
    
    loan_dates_array = []
    for _ in range(total_loan_quantity):
        year = random.choices(years, weights=weights, k=1)[0]
        d = random.choice(dates_by_year[year])
        loan_dates_array.append(d.strftime('%Y-%m-%d'))

    df_loans = clients.copy()
    df_loans['loan_quantity'] = loan_quantity_array
    df_loans = (
        df_loans.loc[df_loans.index.repeat(df_loans['loan_quantity'])]
        .reset_index(drop=True)
        .drop('loan_quantity', axis=1)
    )
    df_loans['loan_id'] = loan_id_array
    df_loans['loan_amount'] = loan_amount_array
    df_loans['loan_date'] = loan_dates_array

    return df_loans

loan_generator(pd.DataFrame({'id': np.arange(1, 50_001)}))