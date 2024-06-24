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


data = [['1', '1', 'N'], ['2', '1', 'Y'], ['2', '2', 'N'], ['3', '3', 'N'], ['4', '2', 'N'], ['4', '3', 'Y'], ['4', '4', 'N']]
employee = pd.DataFrame(data, columns=['employee_id', 'department_id', 'primary_flag']).astype({'employee_id':'Int64', 'department_id':'Int64', 'primary_flag':'object'})

datasets = [employee]
to_r_df(datasets)
