import pandas as pd
import numpy as np
from app.db.postgres import engine

def get_crm_data():
    query = "SELECT * FROM crm_data LIMIT 10"
    df = pd.read_sql(query, engine)
    df.replace({np.nan: None, np.inf: None, -np.inf: None}, inplace=True)
    return df.to_dict(orient="records")