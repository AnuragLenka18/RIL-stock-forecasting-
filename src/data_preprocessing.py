import pandas as pd

def load_data(path):
    df = pd.read_csv(path, parse_dates=['Date'])
    df.sort_values('Date', inplace=True)
    return df

def preprocess_data(df):
    df = df[['Date', 'Open', 'Close']]
    df.set_index('Date', inplace=True)
    df = df.asfreq('B')  # Business day frequency
    df.fillna(method='ffill', inplace=True)
    return df
