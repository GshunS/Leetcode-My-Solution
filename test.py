import pandas as pd

data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions.loc[transactions['state'] == 'approved', 'state_bool'] = 1
    transactions.loc[transactions['state'] != 'approved', 'state_bool'] = 0

    transactions.loc[transactions['state'] == 'approved', 'amount_bool'] = transactions['amount']
    transactions.loc[transactions['state'] != 'approved', 'amount_bool'] = 0
    transactions['trans_date'] = transactions['trans_date'].astype(str)
    transactions['trans_date'] = transactions['trans_date'].str.slice(0, 7)
    return transactions.groupby(['trans_date', 'country'], as_index=False).agg(
        trans_count=('state', 'count'),
        approved_count=('state_bool', 'sum'),
        trans_total_amount=('amount', 'sum'),
        approved_total_amount=('amount_bool', 'sum')
    )


print(monthly_transactions(transactions))
