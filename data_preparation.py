import pandas as pd

def gold_price_data():

"""Open the two .csv files containing the seperate periods of gold prices.
convert the indexes to Date time.
concatenate the two series."""

    first_gold_price = pd.read_csv("/Users/shogun/code/LAMBCS/lewagon_project/data/raw_data/daily_gold_rate.csv", index_col="Date")
    second_gold_price = pd.read_csv("/Users/shogun/code/LAMBCS/lewagon_project/data/raw_data/XAU_1d_data gold to 2025.csv", sep=';', index_col='Date')

    first_gold_price.index = pd.to_datetime(first_gold_price.index)
    second_gold_price.index = pd.to_datetime(second_gold_price.index)

    gold_price_data = pd.concat([first_gold_price.query("Date < '2004-06-11'")['USD'], second_gold_price.query("Date >= '2004-06-11'")["Close"]], axis=0)

    gold_price_data_df = pd.DataFrame(gold_price_data, columns=['closing_gold'])

    gold_price_data_df.to_csv("/Users/shogun/code/LAMBCS/lewagon_project/data/hostorical_gold_price_1985-01-07_2025_07_15.csv")

    return
