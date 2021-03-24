# Model Regression Project

## Project description:
- Identify features to predict the values of single unit properties
- Run statistical tests to identify relationships between features
- Construct a machine learning model to predict property values

## Data Dictionary
|                              | type    | description                                                                |
|:-----------------------------|:--------|:---------------------------------------------------------------------------|
| taxamount                    | float64 | The annual taxes charged for the property                                  |
| lotsizesquarefeet            | float64 | The total square feet of the lot the property is on                        |
| county                       | object  | The county the property is located in                                      |
| taxvaluedollarcnt            | float64 | The total tax assessed value of the property                               |
| calculatedfinishedsquarefeet | float64 | The total square feet of the developed property                            |
| bathroomcnt                  | float64 | The number of bathrooms in the property                                    |
| bedroomcnt                   | float64 | The number of bedrroms in the property                                     |
| age                          | float64 | The age of the developed property                                          |
| tax_rate                     | float64 | The percentage of annual taxes to total tax assessed value of the property |

## Project Plan:
- Import necessary packages and functions
- Acquire and clean data, acquire MVP, split into necessary groupings (Train, test, validate)
- Explore and look over data for relationships/trends
- Run statistical tests to further identify relationships between features
- Additional data cleaning to prepare for modeling
- Experiment with different models to see which are most effective at predicting train data
- Choose best couple models from train to use on validate
- Best model on validate performed on test
- Deliver results

## Instructions for recreation:
- Import all packages and functions
- env.py file with SQL password, username, and host to acquire data
- Use get_zillow_data() function to acquire initial data
- Use prep() function to prepare data for exploration
- Split the data into train, test, and validate
- Plot variables in various forms to form ideas about relationships between data
- Run correlation and t_tests on train dataset between the following groups:
    - calculatedfinishedsquarefeet and taxvaluedollarcnt
    - county and tax_rate
- Use prep_model() function on result of prep() dataframe to prepare data for modeling
- Re-split data into train, test, and validate
- Test models with varying parameters/features for optimization
- Use best models to use on validate set
- Use the best on test data set

## Findings
- Biggest determining factors for single unit property value among most models were bathroom count and age
- Counties presented in the data came from the California counties of Los Angeles, Ventura, and Orange.
- In my statistical tests, it was found that square footage was not independent of property value
- It was also found that there is likely a difference between Los Angeles county tax rate and the overall average county tax rate
- Created a polynomial model that performed better than the baseline