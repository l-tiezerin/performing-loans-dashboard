import pandas as pd
from faker import Faker

fake = Faker()

client_id = range(1, 50_001)
names = [fake.name() for _ in client_id]

df_clients = pd.DataFrame(
    data={
        'client_id': client_id,
        'client_name': names
    }
)

print(df_clients.head())