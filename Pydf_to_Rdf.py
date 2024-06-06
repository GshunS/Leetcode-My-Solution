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
            str1 = str(dataset.iloc[:,count].to_list())[1:-1].replace('Timestamp', 'as_datetime')
            print(f'{col} = c({str1})')
            count += 1
        print('{} = data.frame({})'.format(name, ', '.join(dataset.columns.tolist())))
        print(name)

data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype({'project_id':'Int64', 'employee_id':'Int64'})
data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]]
employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype({'employee_id':'Int64', 'name':'object', 'experience_years':'Int64'})
datasets = [project, employee]
to_r_df(datasets)
