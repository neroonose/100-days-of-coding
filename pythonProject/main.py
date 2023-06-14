#
import pandas as pd

fpath = r'C:\Users\nero.onose\Downloads\products (1).csv'


def sql_creator(file_path: str, table_name: str):
    raw_data = pd.read_csv(file_path)
    col_names = ",  \n".join(raw_data.columns.to_list()[1:])

    statement = f"CREATE TABLE IF NOT EXISTS {table_name} \n({col_names});"
    return statement

    # create a list
    column_names = []
    # iterate through the shape of the table leaving behind the first column
    for i in range(1, df.shape[1]):
        # assign each result into the list
        Col_Name = df.columns[i]

        column_names.append(Col_Name)
    # remove the results from the list
    col = ",".join(column_names)
    # print
    print()


files = [{'products': r'C:\Users\nero.onose\Downloads\products (1).csv'},
         {'branches': r'C:\Users\nero.onose\Downloads\branches.csv'}]
for file in files:
    for key, value in file.items():
        nero = sql_creator(value, key)

    print(nero)


print("hello".upper().lower())