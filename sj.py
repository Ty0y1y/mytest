import pandas as pd
pd.set_option('display.unicode.east_asian_width',True)
def get_dataframe_from_excel():
    df=pd.read_excel('supermarket_sales.xlsx',
                      sheet_name='销售数据',
                      skiprows=1,
                      index_col='订单号'
                     )
    df['小时数']=pd.to_datetime(df["时间"],format="%H:%M:%S").dt.hour
    return df
sale_df=get_dataframe_from_excel()
print("销售数据的前5行如下：")
print(sale_df.head())
print("销售数据各列的详细信息如下：")
sale_df.info()
