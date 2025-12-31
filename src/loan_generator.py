import pandas as pd
import numpy as np
from client_generator import client_generator

def loan_generator(clients):
    rng = np.random.default_rng(42)

    possible_loan_quantity = np.arange(1, 11)
    weights = .5 ** possible_loan_quantity
    weights /= weights.sum()

    loan_quantity_array = rng.choice(possible_loan_quantity, size=50_000, p=weights)
    loan_id_array = rng.choice(np.arange(1_000, 10_000_001), size=loan_quantity_array.sum(), replace=False)

    df_loans = clients.copy()
    df_loans['loan_quantity'] = loan_quantity_array
    df_loans = (
        df_loans.loc[df_loans.index.repeat(df_loans['loan_quantity'])]
        .reset_index(drop=True)
        .drop('loan_quantity', axis=1)
    )
    df_loans['loan_id'] = loan_id_array

    return print(df_loans)

loan_generator(pd.DataFrame({'id': np.arange(1, 50_001)}))