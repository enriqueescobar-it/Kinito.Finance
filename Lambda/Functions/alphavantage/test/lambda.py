import requests
import json

from requests import Response


def handler(event, context):
    ticker: any = event['ticker']
    alpha_vantage_key: any = event['ALPHA_VANTAGE_KEY']  # 'M5TDEVAYFB9PI5WM'
    alpha_listing_url: str = f'https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={alpha_vantage_key}'
    alpha_symbol_url: str = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={alpha_vantage_key}'
    yfinance_searchall_url: str = f'https://query2.finance.yahoo.com/v1/finance/search?q={ticker}'
    yfinance_searchone_url: str = f'https://query1.finance.yahoo.com/v1/finance/search?q={ticker}&quotesCount=1&newsCount=0'
    #f'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=assetProfile'
    return get_yfinance_ticker_type_json(yfinance_searchone_url, ticker)
    return get_yfinance_tickers_types_json(yfinance_searchall_url, ticker)

def get_yfinance_ticker_type_json(yfinance_searchone_url: str, yfinance_ticker: str) -> json:
    yfinance_search_response: Response = requests.get(yfinance_searchone_url)
    yfinance_search_data: any = yfinance_search_response.json()

    if 'quotes' in yfinance_search_data:
        yfinance_search_quotes = yfinance_search_data['quotes']
        if len(yfinance_search_quotes) > 0:
            yfinance_ticker_type = yfinance_search_quotes[0]['quoteType']
            
            return {
                'statusCode': 200,
                'body': json.dumps({'ticker': yfinance_ticker, 'type': yfinance_ticker_type})
            }
    
    return {
        'statusCode': 404,
        'body': json.dumps({'ticker': yfinance_ticker, 'type': 'UNKNOWN'})
    }

def get_yfinance_tickers_types_json(yfinance_searchall_url: str, yfinance_ticker: str) -> json:
    yfinance_search_response: Response = requests.get(yfinance_searchall_url)
    yfinance_search_data: any = yfinance_search_response.json()

    if 'quotes' in yfinance_search_data:
        yfinance_search_quotes = yfinance_search_data['quotes']
        if len(yfinance_search_quotes) > 0:
            yfinance_ticker_type = yfinance_search_quotes[0]['quoteType']
            
            return {
                'statusCode': 200,
                'body': json.dumps({'ticker': yfinance_ticker, 'type': yfinance_ticker_type})
            }
    
    return {
        'statusCode': 404,
        'body': json.dumps({'ticker': yfinance_ticker, 'type': 'UNKNOWN'})
    }

def get_alpha_ticker_json(alpha_symbol_url: str) -> json:
    alpha_symbol_response : Response = requests.get(alpha_symbol_url)

    if alpha_symbol_response.status_code == 200:
        alpha_symbol_response_json: any = alpha_symbol_response.json()
        return {
            'statusCode': 200,
            'body': json.dumps(alpha_symbol_response_json)
        }
    else:
        return {
            'statusCode': alpha_symbol_response.status_code,
            'body': 'Error occurred while retrieving data'
        }


def getall_alpha_ticker_type_json(alpha_listing_url: str) -> json:
    alpha_listing_response: Response = requests.get(alpha_listing_url)

    if alpha_listing_response.status_code == 200:
        alpha_listing_response_json: any = alpha_listing_response.json()
        alpha_listing_types: any = alpha_listing_response_json.get('results', {})

        # Extract the different ticker types from the API response
        unique_listing_type = set(alpha_listing_type['assetType'] for alpha_listing_type in alpha_listing_types)

        # Create a JSON response with the unique ticker types
        unique_listing_types_str: str = json.dumps(list(unique_listing_type))

        return {
            'statusCode': 200,
            'body': unique_listing_types_str
        }
    else:
        return {
            'statusCode': alpha_listing_response.status_code,
            'body': 'Failed to retrieve ticker types'
        }
