from Common.Measures.Portfolio.AbstractPortfolioMeasure import AbstractPortfolioMeasure
from Common.Measures.Time.TimeSpan import TimeSpan
from finquant.portfolio import build_portfolio


class PortfolioFinal(AbstractPortfolioMeasure):

    def __init__(self, y_stocks: list):
        yahoo_list: list = list()
        t_s: TimeSpan = y_stocks[0].TimeSpan
        for y_stock in y_stocks:
            yahoo_list.append(y_stock.Ticker)
        pf = build_portfolio(names=yahoo_list, start_date=t_s.StartDateStr, end_date=t_s.EndDateStr, data_api='yfinance')
        print(pf.data.head(3))
