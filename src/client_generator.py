import pandas as pd
from faker import Faker
import os

fake = Faker(locale='en_US', seed=42)

client_id = range(1, 50_001)
names = [fake.name() for _ in client_id]

df_clients = pd.DataFrame(
    data={
        'client_id': client_id,
        'client_name': names
    }
)

output_path = 'data/clients.csv'
os.makedirs('data', exist_ok=True)

if not os.path.exists(output_path):
    df_clients.to_csv(output_path, index=False)