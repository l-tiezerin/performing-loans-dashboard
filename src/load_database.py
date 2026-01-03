import pandas as pd
from client_generator import client_generator, employee_generator
from loan_generator import loan_generator
import os
from sqlalchemy import create_engine

def load_database():
    df_clients = client_generator()
    df_employees = employee_generator()
    df_loans, df_performing_loans = loan_generator(df_clients)

    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        print("DATABASE_URL not set")
        return

    engine = create_engine(database_url)
    df_clients.to_sql('clients', engine, if_exists='replace', index=False)
    df_employees.to_sql('employees', engine, if_exists='replace', index=False)
    df_loans.to_sql('loans', engine, if_exists='replace', index=False)
    df_performing_loans.to_sql('performing_loans', engine, if_exists='replace', index=False)
    print("Data loaded successfully")