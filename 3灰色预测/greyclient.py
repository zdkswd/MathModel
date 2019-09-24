from greymodel import GrayForecast
import pandas as pd

df=pd.read_csv('data.csv',encoding='gbk')
gf = GrayForecast(df, '数据')
gf.level_check()
gf.forecast(10)
gf.log()
gf.plot()