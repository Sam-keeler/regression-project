import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from datetime import date
import seaborn as sns
from pydataset import data
from env import host, user, password

def get_zillow_data(host = host, user = user, password = password):
    filename = 'zillow.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        db = 'zillow'
        df = pd.read_sql('SELECT taxamount, lotsizesquarefeet, yearbuilt, fips, taxvaluedollarcnt, calculatedfinishedsquarefeet, bathroomcnt, bedroomcnt, propertylandusetypeid, transactiondate FROM properties_2017 JOIN predictions_2017 USING(id) WHERE  propertylandusetypeid IN (261, 262, 263, 273, 275, 276, 279) AND transactiondate >= \'2017-05-01\' AND transactiondate <= \'2017-08-31\'', f'mysql+pymysql://{user}:{password}@{host}/{db}')
        df.to_csv(filename, index = False)
        return df