import argparse
import tushare as ts
data = ts.get_hist_data('600036', start='2019-06-01', end='2019-07-25')
print(data)
data = ts.get_h_data('600036', start='2019-06-01', end='2019-07-25')
print(data)
data = ts.get_today_all()
print(data)
