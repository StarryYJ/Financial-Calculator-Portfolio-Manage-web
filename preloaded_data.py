import yfinance as yf
import os
os.getcwd()



def preload():  # tickers of stocks in DJ
	folder = os.path.exists(os.getcwd()+ '\\data')
	if not folder: 
		os.mkdir('data')
		
	djia = ['MMM', 'AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'DOW',
			'GS', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'MCD', 'MRK', 'MSFT',
			'NKE', 'PG', 'CRM', 'KO', 'HD', 'TRV', 'DIS', 'UNH', 'VZ', 'V',
			'WBA', 'WMT']
	for i in djia:
		df = yf.download(i, start='2019-12-16', end='2020-12-17')
		df['Adj Close'].to_csv('data/' + i + '.csv')


if __name__ == "__main__":
	preload()
	
