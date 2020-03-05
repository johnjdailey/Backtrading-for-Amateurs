import datetime
import backtrader as bt
from strategies import TestStrategy

cerebro = bt.Cerebro()

cerebro.broker.set_cash(1000000)

data = bt.feeds.YahooFinanceCSVData(
    dataname='F.csv',
    # Do not pass values before this date
    fromdate=datetime.datetime(2019, 2, 27),
    # Do not pass values after this date
    todate=datetime.datetime(2020, 2, 26),
    reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

cerebro.addsizer(bt.sizers.FixedSize, stake=1000)

print('Starting Portfolio Value: %2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()