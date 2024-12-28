import sqlite3
import pandas as pd
from sklearn.externals import joblib

class Analyzer():
    
    def__init__(self):
        pass
    
    def get_stock_data() -> pd.DataFrame:
        """
        copies data from database to pandas dataframe for data analysis
        """
        con = sqlite3.connect('stocks.db')
        df = pd.read_sql_query('SELECT * FROM stocks', con)
        con.close()

        return df

    
