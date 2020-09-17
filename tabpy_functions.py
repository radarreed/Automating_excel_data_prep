import pandas as pd

def ffill(df):
    df['Month'] = df['Month'].fillna(method='ffill')
    return df