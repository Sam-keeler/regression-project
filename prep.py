def prep(zillow):
    zillow['age'] = 2021 - zillow.yearbuilt
    zillow.drop(columns = ['propertylandusetypeid', 'transactiondate', 'yearbuilt'], inplace = True)
    zillow.fips.replace({6037: 'Los Angeles', 6059: 'Orange', 6111: 'Ventura'}, inplace = True)
    zillow.rename(columns = {'fips': 'county'}, inplace = True)
    zillow['tax_rate'] = zillow.taxamount / zillow.taxvaluedollarcnt
    zillow.dropna(inplace = True)
    Q1 = zillow['taxvaluedollarcnt'].quantile(0.25)
    Q3 = zillow['taxvaluedollarcnt'].quantile(0.75)
    IQR = Q3 - Q1
    zillow_no_out = zillow[(zillow.taxvaluedollarcnt < (Q3 + IQR)) & (zillow.taxvaluedollarcnt > (Q1 - IQR))]
    Q1 = zillow_no_out['tax_rate'].quantile(0.25)
    Q3 = zillow_no_out['tax_rate'].quantile(0.75)
    IQR = Q3 - Q1
    zillow_no_out = zillow_no_out[(zillow_no_out.tax_rate < (Q3 + IQR)) & (zillow_no_out.tax_rate > (Q1 - IQR))]
    zillow_no_out.drop(columns = ['tax_rate', 'bathroomcnt', 'taxamount'], inplace = True)
    dummies_county = pd.get_dummies(zillow_no_out[['county']], drop_first = True)
    zillow_no_out.drop(columns = ['county'], inplace = True)
    zillow_no_out = pd.concat([zillow_no_out, dummies_county], axis=1)
    scaler_minmax = sklearn.preprocessing.MinMaxScaler()
    scaler_minmax.fit(zillow_no_out)
    zillow_minmax = scaler_minmax.transform(zillow_no_out)
    zillow_minmax = pd.DataFrame(zillow_minmax)
    key = zillow_no_out.columns.tolist()
    zillow_minmax.rename(columns = {i: key[i] for i in range(len(key))} , inplace = True)
    zillow_minmax.drop(columns = ['taxvaluedollarcnt'], inplace = True)
    zillow_no_out.index = zillow_minmax.index
    zillow_minmax['taxvaluedollarcnt'] = zillow['taxvaluedollarcnt']
    zillow_minmax.dropna(inplace = True)
    return zillow_minmax