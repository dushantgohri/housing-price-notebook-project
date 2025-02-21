import pandas as pd
from sqlalchemy import create_engine

def upload_predictions_to_snowflake(predictions_df, table_name, connection_string):
    engine = create_engine(connection_string)
    
    # Upload the predictions DataFrame to Snowflake
    predictions_df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Predictions uploaded to Snowflake table: {table_name}")

if __name__ == "__main__":
    # Example usage
    connection_string = "snowflake://<user>:<password>@<account>/<database>/<schema>"
    predictions_df = pd.read_csv('predictions.csv')  # Assuming predictions are saved in a CSV file
    upload_predictions_to_snowflake(predictions_df, 'housing_price_predictions', connection_string)