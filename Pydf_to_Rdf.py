import pandas as pd


def get_var_name(var):
    for name, value in globals().items():
        if value is var:
            return name


def to_r_df(datasets):
    for dataset in datasets:
        name = get_var_name(dataset)
        count = 0
        print()
        for col in dataset.columns:
            str1 = str(dataset.iloc[:, count].to_list())[1:-1].replace('Timestamp', 'as_datetime')
            print(f'{col} = c({str1})')
            count += 1
        print('{} = data.frame({})'.format(name, ', '.join(dataset.columns.tolist())))
        print(name)


data = [['0', '1'], ['1', '0'], ['2', '0'], ['2', '1']]
followers = pd.DataFrame(data, columns=['user_id', 'follower_id']).astype({'user_id':'Int64', 'follower_id':'Int64'})

datasets = [followers]
to_r_df(datasets)
