import snowflake.connector
import pandas as pd

def fetch_data_from_snowflake():
    # Establish a connection to Snowflake
    conn = snowflake.connector.connect(
        user='dushantgohri',
        password='Dg@17343857148',
        account='pwizmma-ka25931',
        warehouse='compute_wh',
        database='test_datawarehous',
        schema='public'
    )

#     conn_params = {
#     "user": "dushantgohri",
#     "password": "Dg@17343857148",
#     "account": "pwizmma-ka25931",
#     "warehouse": "compute_wh",
#     "database": "test_datawarehouse",
#     "schema": "raw"
# }

    # Fetch training data
    train_query = "SELECT * FROM YOUR_TRAIN_TABLE"
    train_data = pd.read_sql(train_query, conn)
    train_data.to_csv('data/train.csv', index=False)

    # Fetch test data
    test_query = "SELECT * FROM YOUR_TEST_TABLE"
    test_data = pd.read_sql(test_query, conn)
    test_data.to_csv('data/test.csv', index=False)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    fetch_data_from_snowflake()