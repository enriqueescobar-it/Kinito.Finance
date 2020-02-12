#!/usr/bin/python3
import csv

#panda
import pandas as Pan
import datetime as PanDateTime

tgt_start = PanDateTime.datetime(2019, 1, 1)
tgt_stop_ = PanDateTime.datetime.now()

def set_dataframe(yahoo_content):
	if (yahoo_content.empty):
		yahoo_content = "NA"
	else:
		yahoo_content = yahoo_content.to_string()
	return yahoo_content

def set_series(yahoo_content):
	if (yahoo_content.empty):
		yahoo_content = "NA"
		print("\tSERIES\t" + yahoo_content)
	else:
		yahoo_content.to_string()
	return yahoo_content

def set_tuple(yahoo_content):
	if (is_empty(yahoo_content)):
		yahoo_content = "NA"
		print("\tTUPLE\t" + yahoo_content)
	else:
		yahoo_content = ' | '.join([str(elem) for elem in list(yahoo_content)])
	return yahoo_content

def set_dict(yahoo_content):
	if (not yahoo_content):
		yahoo_content = "NA"
	return yahoo_content

#os.path
import os.path as YaOsPath

def get_yfile(yahoo_file, yahoo_symbol):
	y_file = yahoo_file.replace('.', '_' + yahoo_symbol + '.')
	print("#\t" + yahoo_symbol + "\t" + y_file)
	return y_file

#json
import json
import requests
import pprint

def set_yfileJSON(yahoo_file, yahoo_content, yahoo_desc):
	json_file = yahoo_file #+ ".json"
	f = open(yahoo_file, "a")
	f.write('\n' + yahoo_desc + '\n')
	f.close()
	with open(json_file, 'a') as file_pointer:
		json.dump(yahoo_content, file_pointer)

def get_panda_tgt(yahoo_symbol):
	tgt_website = r'https://ca.finance.yahoo.com/quote/' + yahoo_symbol + '/key-statistics?p=' + yahoo_symbol
	#print(tgt_website)
	#html_read = Pan.read_html(tgt_website)
	#html_head = html_read[0]

	#for html_line in html_read[1:]:
	#	html_head = html_head.append(html_line)
	# The data is in column format. Transpose the result to make all data in single row
	#return
	#html_head.set_index(0).T
	return tgt_website

def set_yfile(yahoo_file, yahoo_symbol, yahoo_desc):
	file_exists = YaOsPath.isfile(yahoo_file)
	if file_exists:
		print("#\t" + yahoo_symbol + "\tskipping existing file")
	else: # init file
		print("#\t" + yahoo_symbol + "\tcreating new file")
		f = open(yahoo_file, "w+")
		f.write(">Symbol\n")
		f.write(yahoo_symbol + "\n")
		f.write(">Description\n")
		f.write(yahoo_desc + "\n")
		f.write(">URL\n")
		f.write(get_panda_tgt(yahoo_symbol) + "\n")
		f.write(get_pandr(yahoo_symbol, yahoo_file))
		f.close()

import pprint
def get_the_string(yahoo_content, yahoo_file):
	if (type(yahoo_content) == int):
		print("#\tINT\t" + yahoo_file)
		yahoo_content = str(yahoo_content)
	if (type(yahoo_content) == float):
		print("#\tFLOAT\t" + yahoo_file)
		yahoo_content = str(yahoo_content)
	if (type(yahoo_content) == Pan.DataFrame):
		print("#\tDATA_FRAME\t" + yahoo_file)
		yahoo_content = set_dataframe(yahoo_content)
	if (type(yahoo_content) == Pan.Series):
		print("#\tSERIES\t" + yahoo_file)
		yahoo_content = set_series(yahoo_content)
	if (type(yahoo_content) == tuple):
		print("#\tTUPLE\t" + yahoo_file)
		yahoo_content = set_tuple(yahoo_content)
	if (type(yahoo_content) == dict):
		print("#\tDICT\t" + yahoo_file)
		yahoo_content = set_dict(yahoo_content)
		with open(yahoo_file, 'a') as f_out:
			pprint.pprint(yahoo_content, stream=f_out)
	if (type(yahoo_content) != str):
		print("#\tNOT_STR\t" + yahoo_file)
		yahoo_content = str(yahoo_content)
	return yahoo_content

#from __future__ import print_function
import sys
import time
from yahoofinancials import YahooFinancials as PanYF

tsxFile = 'NYSE/NYSE-y.txt'

def get_yfinancials(yahoo_symbol, yahoo_file, yahoo_list):
	yahoo_head = ">yahoofinancials | "
	float_peratio = PanYF(yahoo_symbol).get_pe_ratio()
	print("#\t" + yahoo_symbol + "\tPE ratio is " + str(type(float_peratio)))
	if (type(float_peratio) != float):
		print("#\t" + yahoo_symbol + "\tis suffering losses")
	else:
		print("#\t" + yahoo_symbol + "\tis being investigated")
		yahoo_list[3] = get_the_string(float_peratio, yahoo_file)
		float_num_sh_out = PanYF(yahoo_symbol).get_num_shares_outstanding(price_type='current')
		yahoo_list[4] = get_the_string(float_num_sh_out, yahoo_file)
		int_opera_income = PanYF(yahoo_symbol).get_operating_income()
		yahoo_list[5] = get_the_string(int_opera_income, yahoo_file)
		int_totop_income = PanYF(yahoo_symbol).get_total_operating_expense()
		yahoo_list[6] = get_the_string(int_totop_income, yahoo_file)
		int_total_revenu = PanYF(yahoo_symbol).get_total_revenue()
		yahoo_list[7] = get_the_string(int_total_revenu, yahoo_file)
		int_costofrevenu = PanYF(yahoo_symbol).get_cost_of_revenue()
		yahoo_list[8] = get_the_string(int_costofrevenu, yahoo_file)
		int_income_b4tax = PanYF(yahoo_symbol).get_income_before_tax()
		yahoo_list[9] = get_the_string(int_income_b4tax, yahoo_file)
		int_incometaxexp = PanYF(yahoo_symbol).get_income_tax_expense()
		yahoo_list[10] = get_the_string(int_incometaxexp, yahoo_file)
		int_gross_profit = PanYF(yahoo_symbol).get_gross_profit()
		yahoo_list[11] = get_the_string(int_gross_profit, yahoo_file)
		int_netincfromcontops = PanYF(yahoo_symbol).get_net_income_from_continuing_ops()
		yahoo_list[12] = get_the_string(int_netincfromcontops, yahoo_file)
		_research_n_dev_ = PanYF(yahoo_symbol).get_research_and_development()
		yahoo_list[13] = get_the_string(_research_n_dev_, yahoo_file)
		float_prevclosing = PanYF(yahoo_symbol).get_prev_close_price()
		yahoo_list[14] = get_the_string(float_prevclosing, yahoo_file)
		float_open_price = PanYF(yahoo_symbol).get_open_price()
		yahoo_list[15] = get_the_string(float_open_price, yahoo_file)
		float_curr_price = PanYF(yahoo_symbol).get_current_price()
		yahoo_list[16] = get_the_string(float_curr_price, yahoo_file)
		str_stock_exch = PanYF(yahoo_symbol).get_stock_exchange()
		yahoo_list[17] = get_the_string(str_stock_exch, yahoo_file)
		int_market_cap = PanYF(yahoo_symbol).get_market_cap()
		yahoo_list[18] = get_the_string(int_market_cap, yahoo_file)
		str_currency = PanYF(yahoo_symbol).get_currency()
		yahoo_list[19] = get_the_string(str_currency, yahoo_file)
		str_annualavgdivyield = PanYF(yahoo_symbol).get_annual_avg_div_yield()
		yahoo_list[20] = get_the_string(str_annualavgdivyield, yahoo_file)
		float_5yravgdivyield = PanYF(yahoo_symbol).get_five_yr_avg_div_yield()
		yahoo_list[21] = get_the_string(float_5yravgdivyield, yahoo_file)
		float_dividendrate = PanYF(yahoo_symbol).get_dividend_rate()
		yahoo_list[22] = get_the_string(float_dividendrate, yahoo_file)
		float_annualavgdivrate = PanYF(yahoo_symbol).get_annual_avg_div_rate()
		yahoo_list[23] = get_the_string(float_annualavgdivrate, yahoo_file)
		float_50daymovingavg = PanYF(yahoo_symbol).get_50day_moving_avg()
		yahoo_list[24] = get_the_string(float_50daymovingavg, yahoo_file)
		float_200daymovingavg = PanYF(yahoo_symbol).get_200day_moving_avg()
		yahoo_list[25] = get_the_string(float_200daymovingavg, yahoo_file)
		float_beta = PanYF(yahoo_symbol).get_beta()
		yahoo_list[26] = get_the_string(float_beta, yahoo_file)
		float_payoutratio = PanYF(yahoo_symbol).get_payout_ratio()
		yahoo_list[27] = get_the_string(float_payoutratio, yahoo_file)
		float_pricetosales = PanYF(yahoo_symbol).get_price_to_sales()
		yahoo_list[28] = get_the_string(float_pricetosales, yahoo_file)
		str_exdividenddate = PanYF(yahoo_symbol).get_exdividend_date()
		yahoo_list[29] = get_the_string(str_exdividenddate, yahoo_file)
		int_bookvalue = PanYF(yahoo_symbol).get_book_value()
		yahoo_list[30] = get_the_string(int_bookvalue, yahoo_file)
		int_e_bit = PanYF(yahoo_symbol).get_ebit()
		yahoo_list[31] = get_the_string(int_e_bit, yahoo_file)
		int_netincome = PanYF(yahoo_symbol).get_net_income()
		yahoo_list[32] = get_the_string(int_netincome, yahoo_file)
		float_earningspershare = PanYF(yahoo_symbol).get_earnings_per_share()
		yahoo_list[33] = get_the_string(float_earningspershare, yahoo_file)
		_interestexpense = PanYF(yahoo_symbol).get_interest_expense()
		yahoo_list[34] = get_the_string(_interestexpense, yahoo_file)
		_currentchange = PanYF(yahoo_symbol).get_current_change()
		yahoo_list[35] = get_the_string(_currentchange, yahoo_file)
		_currentprcntchange = PanYF(yahoo_symbol).get_current_percent_change()
		yahoo_list[36] = get_the_string(_currentprcntchange, yahoo_file)
		'''
		f = open(yahoo_file, "a")
		# FLOAT
		yahoo_header = yahoo_head + "PE Ratio [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_num_shares_outstanding(price_type='current')
		yahoo_header = yahoo_head + "Number Shares Outstanding (current) [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_operating_income()
		yahoo_header = yahoo_head + "Operating Income [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_total_operating_expense()
		yahoo_header = yahoo_head + "Total Operating Expense [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_total_revenue()
		yahoo_header = yahoo_head + "Total Revenue [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_cost_of_revenue()
		yahoo_header = yahoo_head + "Cost of Revenue [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_income_before_tax()
		yahoo_header = yahoo_head + "Income Before Tax [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_income_tax_expense()
		yahoo_header = yahoo_head + "Income Tax Expense [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_gross_profit()
		yahoo_header = yahoo_head + "Gross Profit [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_net_income_from_continuing_ops()
		yahoo_header = yahoo_head + "Net Income from Continuing Ops [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# ?
		yahoo_content = PanYF(yahoo_symbol).get_research_and_development()
		yahoo_header = yahoo_head + "RnD [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_prev_close_price()
		yahoo_header = yahoo_head + "Previous Close Price [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_open_price()
		yahoo_header = yahoo_head + "Open Price [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_current_price()
		yahoo_header = yahoo_head + "Current Price [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# STR
		yahoo_content = PanYF(yahoo_symbol).get_stock_exchange()
		yahoo_header = yahoo_head + "Stock Exchange [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_market_cap()
		yahoo_header = yahoo_head + "Market Cap [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# STR
		yahoo_content = PanYF(yahoo_symbol).get_currency()
		yahoo_header = yahoo_head + "Currency [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# STR
		yahoo_content = PanYF(yahoo_symbol).get_annual_avg_div_yield()
		yahoo_header = yahoo_head + "Annual Average Div Yield [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_five_yr_avg_div_yield()
		yahoo_header = yahoo_head + "5 Year Average Div Yield [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_dividend_rate()
		yahoo_header = yahoo_head + "Dividend Rate [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_annual_avg_div_rate()
		yahoo_header = yahoo_head + "Annual Average Div Rate [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_50day_moving_avg()
		yahoo_header = yahoo_head + "50 Day Moving Average [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_200day_moving_avg()
		yahoo_header = yahoo_head + "200 Day Moving Average [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_beta()
		yahoo_header = yahoo_head + "Beta [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_payout_ratio()
		yahoo_header = yahoo_head + "Payout Ratio [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_price_to_sales()
		yahoo_header = yahoo_head + "Price to Sales [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# STR
		yahoo_content = PanYF(yahoo_symbol).get_exdividend_date()
		yahoo_header = yahoo_head + "Exdividend Date [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_book_value()
		yahoo_header = yahoo_head + "Book Value [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_ebit()
		yahoo_header = yahoo_head + "eBit [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# INT
		yahoo_content = PanYF(yahoo_symbol).get_net_income()
		yahoo_header = yahoo_head + "Net Income [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# FLOAT
		yahoo_content = PanYF(yahoo_symbol).get_earnings_per_share()
		yahoo_header = yahoo_head + "Earnings per Share [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		#
		yahoo_content = PanYF(yahoo_symbol).get_interest_expense()
		yahoo_header = yahoo_head + "Interest Expense [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		#
		yahoo_content = PanYF(yahoo_symbol).get_current_change()
		yahoo_header = yahoo_head + "Current Change [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		#
		yahoo_content = PanYF(yahoo_symbol).get_current_percent_change()
		yahoo_header = yahoo_head + "Current Percent Change [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# CLOSE
		f.close()'''
		# DICT
		yahoo_content = PanYF(yahoo_symbol).get_financial_stmts('annual', 'balance', reformat=False)
		yahoo_header = yahoo_head + "Financial Statements (annual,balance) [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		yahoo_content = PanYF(yahoo_symbol).get_stock_price_data(reformat=False)
		yahoo_header = yahoo_head + "Stock Price Data [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		yahoo_content = PanYF(yahoo_symbol).get_stock_earnings_data(reformat=False)
		yahoo_header = yahoo_head + "Stock Earnings Data [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		yahoo_content = PanYF(yahoo_symbol).get_summary_data(reformat=False)
		yahoo_header = yahoo_head + "Summary Data [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		yahoo_content = PanYF(yahoo_symbol).get_stock_quote_type_data()
		yahoo_header = yahoo_head + "Stock Quote Type Data [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		yahoo_content = PanYF(yahoo_symbol).get_historical_price_data('2019-01-01', '2020-01-01', 'monthly')
		yahoo_header = yahoo_head + "Historical Price Data (last year, monthly) [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		yahoo_content = PanYF(yahoo_symbol).get_daily_dividend_data('2019-01-01', '2020-01-01')
		yahoo_header = yahoo_head + "Daily Dividend Data (last year) [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		yahoo_content = PanYF(yahoo_symbol).get_key_statistics_data()
		yahoo_header = yahoo_head + "Key Statistics Data [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		get_yfinance(yahoo_symbol, ">yfinance | ", yahoo_file)
		'''
		# FLOAT yahoo_content = PanYF(yahoo_symbol).get_yearly_high()
		yahoo_header = yahoo_head + "Yearly High [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		# FLOAT yahoo_content = PanYF(yahoo_symbol).get_yearly_low()
		yahoo_header = yahoo_head + "Yearly Low [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		# yahoo_content = PanYF(yahoo_symbol).get_current_volume()
		yahoo_header = yahoo_head + "Current Volume [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		# INT yahoo_content = PanYF(yahoo_symbol).get_three_month_avg_daily_volume()
		yahoo_header = yahoo_head + "3 Month Average Average Daily Volume [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		# INT yahoo_content = PanYF(yahoo_symbol).get_ten_day_avg_daily_volume()
		yahoo_header = yahoo_head + "10 Day Average Daily Volume [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		#get_the_string(yahoo_file, "Daily Low", PanYF(yahoo_symbol).get_daily_low())
		#get_the_string(yahoo_file, "Daily High", PanYF(yahoo_symbol).get_daily_high())'''

#quandl
import quandl as Qndl
#
def get_quandl(yahoo_symbol):
	qdl = Qndl.get(yahoo_symbol,
			start_date="2019-01-01",
			end_date="2020-01-01")
	print(type(qdl))

#panda_datareader
import pandas_datareader as PanDR
import datetime as PanDateTime

def get_pandr(yahoo_symbol, yahoo_file):
	yahoo_head = ">pandas_datareader | "
	yahoo_content = PanDR.get_data_yahoo(yahoo_symbol,
									start=PanDateTime.datetime(2019, 1, 1),
									end=PanDateTime.datetime(2020, 1, 1))
	yahoo_header = yahoo_head + "Last Year [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
	return yahoo_header

#yfinance
import yfinance as YaFin

def get_yfinance(yahoo_symbol, yahoo_desc, yahoo_file):
	yahoo_head = yahoo_desc
	f = open(yahoo_file, "a")
	# DATA_FRAME
	yahoo_content = YaFin.Ticker(yahoo_symbol).history(period="min")
	yahoo_header = yahoo_head + "History (min) [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
	f.write(yahoo_header)
	# SERIES
	yahoo_content = YaFin.Ticker(yahoo_symbol).dividends
	yahoo_header = yahoo_head + "Dividends [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
	f.write(yahoo_header)
	# SERIES
	yahoo_content = YaFin.Ticker(yahoo_symbol).splits
	yahoo_header = yahoo_head + "Splits [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
	f.write(yahoo_header)
	try:
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).financials
		yahoo_header = yahoo_head + "Financials [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).quarterly_financials
		yahoo_header = yahoo_head + "Financials Quarterly [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).major_holders
		yahoo_header = yahoo_head + "Major Holders [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).institutional_holders
		yahoo_header = yahoo_head + "Institutional Holders [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).balance_sheet
		yahoo_header = yahoo_head + "Balance Sheet [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).quarterly_balance_sheet
		yahoo_header = yahoo_head + "Quarterly Balance Sheet [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).cashflow
		yahoo_header = yahoo_head + "Cashflow [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).quarterly_cashflow
		yahoo_header = yahoo_head + "Quarterly Cashflow [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).earnings
		yahoo_header = yahoo_head + "Earnings [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).quarterly_earnings
		yahoo_header = yahoo_head + "Quarterly Earnings [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# DATA_FRAME
		yahoo_content = YaFin.Ticker(yahoo_symbol).calendar
		yahoo_header = yahoo_head + "Calendar [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
		f.write(yahoo_header)
		# CLOSE
		f.close()
		# DICT
		yahoo_content = YaFin.Ticker(yahoo_symbol).info
		yahoo_header = yahoo_head + "yfinance Info [" + str(type(yahoo_content)) + "]\n" + get_the_string(yahoo_content, yahoo_file) + "\n"
	except:
		print(yahoo_desc + " PROCESSING ERROR SKIPPING...")
	'''#get_the_string(yahoo_file, ">yfinance | Actions", yfin.actions)
	##get_the_string(yahoo_file, ">yfinance | Sustainability", yfin.sustainability)
	#get_the_string(yahoo_file, ">yfinance | Recommendations", yfin.recommendations)
	#get_the_string(yahoo_file, ">yfinance | International Securities Identification Number", yfin.isin)
	##get_the_string(yahoo_file, ">yfinance | Options Expirations", yfin.options)'''

print("#\t" + tsxFile)

csv_list = list()
csv_list = ["NA"]*47 # ["NA" for i in range(47)]
headlist = ['Symbol', 'Description', 'URL', 'PEratio', 'NbSharesOutstandingCurrent', 'OperatingIncome',
	'TotalOperatingExpense', 'TotalRevenue', 'CostOfRevenue', 'IncomeBeforeTax', 'IncomeTaxExpense',
	'Gross Profit', 'NetIncomeFromContinuingOps', 'R&D', 'PreviousClosePrice', 'OpenPrice', 'CurrentPrice',
	'10DayAverageDailyVolume', '3MonthAverageAverageDailyVolume', 'StockExchange', 'MarketCap', 'Currency',
	'YearlyHigh', 'YearlyLow', 'AnnualAverageDivYield', '5YearAverageDivYield', 'DividendRate',
	'AnnualAverageDivRate', '50DayMovingAverage', '200DayMovingAverage', 'Beta', 'PayoutRatio',
	'PriceToSales', 'ExdividendDate', 'BookValue', 'eBit', 'NetIncome', 'EarningsPerShare',
	'CurrentChange', 'CurrentPercentChange', 'CurrentVolume', '_1', '_2', '_3', '_4', '_5', '_6']

with open(tsxFile) as aCsvFile:
	#readCSV = csv.reader(aCsvFile, delimiter='\t')
	readCSV = csv.DictReader(aCsvFile, delimiter='\t')

	yahoo_csvfile = tsxFile + ".csv"
	with open(yahoo_csvfile, mode='w') as csv_yfile:
		writer = csv.DictWriter(csv_yfile, fieldnames = headlist, delimiter = ';', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
		writer.writeheader()

	for readCSVLine in readCSV:
		readCSVfile = get_yfile(tsxFile, readCSVLine['Symbol'])
		csv_list[0] = readCSVLine['Symbol']
		csv_list[1] = readCSVLine['Description']
		csv_list[2] = get_panda_tgt(readCSVLine['Symbol'])
		set_yfile(readCSVfile, readCSVLine['Symbol'], readCSVLine['Description'])
		get_yfinancials(readCSVLine['Symbol'], readCSVfile, csv_list)
		pprint.pprint(csv_list)
		# Appending a row to csv with missing entries
		f = open(yahoo_csvfile, "a")
		f.write(';'.join(csv_list) + "\n")
		f.close()
