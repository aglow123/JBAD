from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


if __name__ == '__main__':

    df1 = pd.read_csv(r'dane/Plant_1_Generation_Data.csv')
    df2 = pd.read_csv(r'dane/Plant_2_Generation_Data.csv')
    df2['DATE_TIME'] = df2['DATE_TIME'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')) # nie wystarczy użyć parse_dates przy wczytywaniu?
    df2['DATE_TIME'] = df2['DATE_TIME'].apply(lambda x: datetime.strftime(x, '%d-%m-%Y %H:%M'))

    df = pd.concat([df1, df2])
    df = df.replace(r'^s*$', float('NaN'), regex=True)
    df = df.dropna()

    df['DATE_TIME'] = pd.to_datetime(df['DATE_TIME'])
    df_week1 = df.loc[(df['DATE_TIME'] >= '15-05-2020 00:00') & (df['DATE_TIME'] < '22-05-2020 00:00')].reset_index()
    df1_week1 = df_week1.loc[(df_week1['SOURCE_KEY'] == 'uHbuxQJl8lW7ozc')]
    df_avg = df_week1[['DATE_TIME', 'AC_POWER']]
    df_avg['AVG'] = df_avg.groupby('DATE_TIME')['AC_POWER'].transform(np.average)
    df_avg1 = df_week1[['DATE_TIME', 'AC_POWER']]
    df_avg1 = df_avg1.groupby('DATE_TIME')['AC_POWER'].mean().reset_index()

    plt.plot(df_avg1['DATE_TIME'], df_avg1['AC_POWER'], label='AVG')
    plt.plot(df1_week1['DATE_TIME'], df1_week1['AC_POWER'], label='generator 1')
    plt.legend()
    plt.show()

    df_week1_faulty = df_week1[['DATE_TIME', 'SOURCE_KEY']].where((df_week1['AC_POWER'] < 0.8 * df_avg['AVG']))
    df_week1_faulty = df_week1_faulty.dropna()
    print(df_week1_faulty.SOURCE_KEY.value_counts().head(10))
    
