import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    r"C:\Users\HP\Documents\PORTAFOLIO_sql\AB_NYC_2019_clean.csv",
    encoding="latin1"
)

engine = create_engine("postgresql+psycopg2://postgres:postgres123@localhost:5432/airbnb_db")

df.to_sql("airbnb", engine, if_exists="replace", index=False)

print("Datos cargados correctamente")