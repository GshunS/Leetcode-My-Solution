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
            str1 = str(dataset.iloc[:, count].to_list())[1:-1].replace('Timestamp', 'as_datetime').replace('<NA>', 'NA')
            print(f'{col} = c({str1})')
            count += 1
        print('{} = data.frame({})'.format(name, ', '.join(dataset.columns.tolist())))
        print(name)


data = [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames']]
seat = pd.DataFrame(data, columns=['id', 'student']).astype({'id':'Int64', 'student':'object'})

datasets = [seat]
to_r_df(datasets)
