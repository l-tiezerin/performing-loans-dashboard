import pandas as pd
import numpy as np
import random
import math
from client_generator import client_generator

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

    df_loans = clients.copy()
    df_loans['loan_quantity'] = loan_quantity_array
    df_loans = (
        df_loans.loc[df_loans.index.repeat(df_loans['loan_quantity'])]
        .reset_index(drop=True)
        .drop('loan_quantity', axis=1)
    )
    df_loans['loan_id'] = loan_id_array
    df_loans['loan_amount'] = loan_amount_array

    return print(df_loans, df_loans['loan_amount'].describe())

loan_generator(pd.DataFrame({'id': np.arange(1, 50_001)}))