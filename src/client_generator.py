import pandas as pd
from faker import Faker

def client_generator():
    Faker.seed(42)
    fake = Faker(locale='en_US')

    client_id = range(1, 50_001)
    names = [fake.name() for _ in client_id]

    df_clients = pd.DataFrame({
        'client_id': client_id,
        'client_name': names
    })
    
    return df_clients

def employee_generator():
    return client_generator().sample(150, random_state=42).reset_index(drop=True)