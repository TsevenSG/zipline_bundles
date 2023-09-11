import pandas as pd
import pytz

SYMBOLS_64_STOCKS = {
    'SPY': 'AMEX:SPY',
    'RSP': 'AMEX:RSP',
    'QQQ': 'NASDAQ:QQQ',
    'QQQE': 'NASDAQ:QQQE',
    'DIA': 'AMEX:DIA',
    'IWM': 'AMEX:IWM',
    'VO': 'AMEX:VO',
    'XLC': 'AMEX:XLC',
    'XLP': 'AMEX:XLP',
    'XLY': 'AMEX:XLY',
    'XLE': 'AMEX:XLE',
    'XLF': 'AMEX:XLF',
    'XLV': 'AMEX:XLV',
    'XLI': 'AMEX:XLI',
    'XLB': 'AMEX:XLB',
    'XLRE': 'AMEX:XLRE',
    'XLK': 'AMEX:XLK',
    'XLU': 'AMEX:XLU',
    'BIL': 'AMEX:BIL',
    'SHY': 'NASDAQ:SHY',
    'IEI': 'NASDAQ:IEI',
    'IEF': 'NASDAQ:IEF',
    'TLT': 'NASDAQ:TLT',
    'EDV': 'AMEX:EDV',
    'HYG': 'AMEX:HYG',
    'LQD': 'AMEX:LQD',
    'FALN': 'NASDAQ:FALN',
    'FLOT': 'AMEX:FLOT',
    'MUB': 'AMEX:MUB',
    'EMLC': 'AMEX:EMLC',
    'EMB': 'NASDAQ:EMB',
    'VEU': 'AMEX:VEU',
    'EZU': 'AMEX:EZU',
    'EWI': 'AMEX:EWI',
    'EWP': 'AMEX:EWP',
    'EWQ': 'AMEX:EWQ',
    'EWG': 'AMEX:EWG',
    'EPOL': 'AMEX:EPOL',
    'EZA': 'AMEX:EZA',
    'EWJ': 'AMEX:EWJ',
    'DXJ': 'AMEX:DXJ',
    'ASHR': 'AMEX:ASHR',
    'FXI': 'AMEX:FXI',
    'ASHS': 'AMEX:ASHS',
    'EWH': 'AMEX:EWH',
    'EWS': 'AMEX:EWS',
    'EIDO': 'AMEX:EIDO',
    'THD': 'AMEX:THD',
    'EWM': 'AMEX:EWM',
    'KWEB': 'AMEX:KWEB',
    'SCJ': 'AMEX:SCJ',
    'EWZ': 'AMEX:EWZ',
    'EWZS': 'NASDAQ:EWZS',
    'EWW': 'AMEX:EWW',
    'ECH': 'AMEX:ECH',
    'EWC': 'AMEX:EWC',
    'GSG': 'AMEX:GSG',
    'USO': 'AMEX:USO',
    'CPER': 'AMEX:CPER',
    'UNL': 'AMEX:UNL',
    'UNG': 'AMEX:UNG',
    'DBA': 'AMEX:DBA',
    'WEAT': 'AMEX:WEAT',
}

SYMBOLS_LATIN_AMERICA = {
    'EWZ': 'AMEX:EWZ',
    'EWW': 'AMEX:EWW',
    'ILF': 'AMEX:ILF',
    'IEF': 'NASDAQ:IEF',
    'TLT': 'NASDAQ:TLT',
    'CL1!': 'NYMEX:CL1!',
    'HG1!': 'COMEX:HG1!',
    'IRX.P': 'CBOE:IRX.P',
    'BRINTR': 'ECONOMICS:BRINTR',
}

SYMBOLS = {
    'SPX': 'SP:SPX',
    **SYMBOLS_64_STOCKS,
    **SYMBOLS_LATIN_AMERICA,
}

MISSING_SESSIONS = {
    'SPX': [
        '1994-12-30',
        '1995-01-19',
        '1995-01-20',
    ],
    'EWZ': [
        '2000-07-24',
        '2000-07-25',
        '2000-07-26',
        '2000-08-08',
        '2000-08-09',
        '2000-08-14',
        '2000-08-16',
        '2000-08-22',
        '2000-08-23',
        '2000-08-30',
        '2000-09-28',
        '2000-10-18',
        '2000-10-24',
        '2000-10-27',
        '2000-10-30',
        '2000-11-10',
        '2000-11-15',
        '2000-11-20',
        '2000-11-21',
        '2000-11-22',
        '2000-11-24',
        '2000-11-29',
        '2000-12-01',
        '2000-12-05',
        '2000-12-26',
        '2001-01-08',
        '2001-03-19',
        '2001-04-12',
        '2001-04-16',
        '2001-05-11',
        '2001-06-13',
        '2001-08-15',
        '2001-10-12',
    ],
    'EWW': [
        '1996-06-10',
        '1996-06-13',
        '1996-06-17',
        '1996-07-19',
        '1996-08-09',
        '1996-11-05',
        '1996-12-24',
        '1997-04-04',
        '1997-04-21',
        '1998-07-10',
        '2000-05-05',
    ],
    'ILF': [
        '2001-10-30',
        '2001-11-05',
        '2001-11-09',
        '2001-11-21',
        '2001-11-23',
        '2001-12-07',
        '2001-12-14',
        '2001-12-17',
        '2001-12-18',
        '2001-12-20',
        '2002-01-09',
        '2002-01-14',
        '2002-01-15',
        '2002-01-29',
        '2002-02-04',
        '2002-02-07',
        '2002-02-11',
        '2002-02-12',
        '2002-02-25',
        '2002-04-26',
        '2002-06-06',
        '2002-07-15',
        '2002-07-19',
        '2002-08-13',
        '2002-08-21',
        '2002-08-22',
        '2002-08-28',
        '2002-08-29',
        '2002-09-05',
        '2002-09-11',
        '2002-09-13',
        '2002-09-17',
        '2002-09-20',
        '2002-10-02',
        '2002-11-15',
        '2003-02-11',
        '2003-03-28',
        '2003-07-09',
    ],
}

EXTRA_SESSIONS = {
    'SPX': [
        '1991-05-27',
        '2001-09-11',
    ],
}

TZ_CST = pytz.timezone('America/Chicago')

def get_downloader(start_date,
                   end_date,
                   granularity='daily',):
    """returns a downloader closure for yahoo
    :param start_date: the first day on which dat are downloaded
    :param end_date: the last day on which data are downloaded
    :param granularity: the frequency of price data, 'D' for daily and 'M1' for 1-minute data
    :type start_date: str in format YYYY-MM-DD
    :type end_date: str in format YYYY-MM-DD
    :type granularity: str
    """

    def downloader(symbol):
        """downloads symbol price data using yahoo REST API
        :param symbol: the symbol name
        :type symbol: str
        """

        if symbol not in SYMBOLS:
            raise ValueError(f'Not support symbol {symbol}')

        tv = TradingView(market='cfd')

        df = tv.historical_charts(symbol=SYMBOLS[symbol], interval='1D', total_candle=10000, charts=[], adjustment='dividends')

        timestamps = pd.to_datetime(df['timestamp_ts'], unit='s').dt.tz_localize('UTC').dt.tz_convert(TZ_CST)
        df['date'] = pd.to_datetime(timestamps.dt.date)
        df.set_index('date', drop=True, inplace=True)
        df.drop('timestamp_ts', inplace=True, axis=1)

        df['dividend'] = 0
        df['split'] = 1

        for i in MISSING_SESSIONS.get(symbol, []):
            if i not in df.index:
                df_insert = df.loc[:i].tail(1).copy()
                df_insert.index = [pd.to_datetime(i)]
                df = pd.concat([df.loc[:i], df_insert, df.loc[i:]])

        df.drop(EXTRA_SESSIONS.get(symbol, []), inplace=True)

        df = df[start_date:end_date]

        print(df.head(3))
        print('...')
        print(df.tail(3))

        return df

    return downloader


#@title Define TradingView class

import json
import random
import re
import string
from datetime import datetime
from typing import Dict, List

import pandas as pd
import pytz
from requests import get, post
from websocket import create_connection

_GLOBAL_URL_ = 'https://scanner.tradingview.com/global/scan'
_API_URL_ = 'https://symbol-search.tradingview.com/symbol_search'
_WS_URL_ = 'wss://data.tradingview.com/socket.io/websocket?&type=chart'

CHARTS_SETTINGS = {
    'ema10': ['Script@tv-scripting-101!',{'text':'bmI9Ks46_u96awLDSJj8c4xVHubmEMw==_E3G6GqoJr5rLISOgO9nBsoc2e4nLvKBi1q5InR7AttexejdPJoAOC8z/vvUAqlCMpPiv11uwGy2v0EG7phDcDFZiaEKMt/1ooB+5hPaSKK7EuUzKTIGLFzbLtwjwO5Z7jR11jP1Z2MsAt9cN0smrwQMTjphpEDRVvzDqBcB2wZRR7BxQeQ9j7ynKMseInC5G34ToyLmrle0+4Dcw9IhWNkvpGLKhODeEIdjlfm6ZzEAu3cuuLIx9Kn1f1h6AdSVccLpVDzTy67dQ9TanhaaIy5Ogz+kuRYKTkkP63IaXvEn03t29DDUoWMxzQolZuBW6vDVAbHMgPm52yHN88uvJ5px4IGDbuRdJlTLrMpbgG4SAP+DWhKL6wbsu9MfYfe4bGMzfvF7vE/ltqlycHIHIjOS2SfFrqxmVg4eH1+V+/7g0JbnCvSJAeY/RKUCx+jJZa+Gm0mvhmvz+abYWJLpqTpBctZ8kYI+6EGVXgshUZrkahn+S0oGnvwOB4NzLMCSX9NLidpDZKuDuI2Whfb08toOkoGiF8JYhvnotLZSDa0DTDhwZtqQf0hAChG/3RK42S75LxcZwyTl39emlxdU9uDoDV+d/NHZFao+FSoNhSkTsqOnfuVp5l3V1yop8Psh64sbs2A1cGqu1','pineId':'STD;EMA','pineVersion':'29.0','pineFeatures':{'v':'{\'indicator\':1,\'plot\':1,\'ta\':1}','f':True,'t':'text'},'in_0':{'v':10,'f':True,'t':'integer'},'in_1':{'v':'close','f':True,'t':'source'},'in_2':{'v':0,'f':True,'t':'integer'},'in_3':{'v':'EMA','f':True,'t':'text'},'in_4':{'v':5,'f':True,'t':'integer'},'in_5':{'v':'','f':True,'t':'resolution'},'in_6':{'v':True,'f':True,'t':'bool'}}],
    'ema21': ['Script@tv-scripting-101!',{'text':'bmI9Ks46_iAX8exg0i/mBcDvY1smolQ==_jO5cug1NHY+z8s0TpdR7Fev6EEMhjfmTU5mbl5iuXE4UOVqejOvpDjiTL5t3fgGOAjkPxvD/uGIuqepaXnEzXZf3Dfcivitq36RSeVQJZkcjMjW9VjSBs2JBC46Z2XEHj1oKNZSZOQlx1NXqJiPhl4wEzpiWIDdgSG2mxoZXjp+4Bq9+C9cMfH0E9t8pFWkvKeckFaN5P8ZtdAR8k/UBSaMd0r68pvEpiLdujfRKb2xjbIQMsnJzqq0/BRMx0rFzK1OHtZLyqaxdHDjIsmwVmyd2OwzJg498v08fSIrlK5VNnlrxk/RUc+ZVrWVY/eH4XmqMuzaNha3HtFUO3wjQip8ISjaWgv+WwGPAnMgVVWSSJrZ9Urtj6+NIbwCRctEaMLKzHI01uk8+JXlzs5pqjzmAyaXvgMkKVvhp5+NjRxKHyHfCD9Gd+UNN8QoAPnRVied3ETVygHjvK6eoD9Wb5TvS9U4sWoShZ8QBX28FinVjbNDYxq/RUTrcevujlasFaD7Y4gbGqakbVBjJx+xNVzbzA4usJMEeCOd9ahtX2HtJdajXxFZkZPImRk+kMtuNSElCq2E10PSn6jFEcHYnOkwF43wDilGsMHWJDI9gXr4nCUqfWBBn8XPrOJVdWyZ7GIxOl9ZOn1ix','pineId':'STD;EMA','pineVersion':'29.0','pineFeatures':{'v':'{\'indicator\':1,\'plot\':1,\'ta\':1}','f':True,'t':'text'},'in_0':{'v':21,'f':True,'t':'integer'},'in_1':{'v':'close','f':True,'t':'source'},'in_2':{'v':0,'f':True,'t':'integer'},'in_3':{'v':'EMA','f':True,'t':'text'},'in_4':{'v':5,'f':True,'t':'integer'},'in_5':{'v':'','f':True,'t':'resolution'},'in_6':{'v':True,'f':True,'t':'bool'}}],
    'ema50': ['Script@tv-scripting-101!',{'text':'bmI9Ks46_YgiQhsSwDdbNYHsEzTaxnA==_tysyiC9xdsEwtdmdMBSVgXuVvcZQ9j6XhIppaillwsxzP5xbNHizoC2fq0d6Q6EZeh3JWFos4nGmxiOETJ4ncnF0L/i6laHxlvePKlj2JEbxW5NGFl5l2KgufioukfuvBYZK/wIWE/3hLrlxXITNc1MWs10LKta7PyhbyJ2gW6G8S+VU0P4L4JBVQurjsKg7vFM9IiSGgZ1MYb655UzYrm9q4VuIlFVj3wQsYj+xf2lK947wZETX1p8T3moRqYmpZ32GT6V5Krk2pVttLcUIAu1pzUOC6cw1f7PNI7dmOskToyk4TpxiVnqbZRRmj2N+vPdb/nXCSQOLH3fX3McEz6uguxb0MBQgnbCMrdV6bDtVB5xiCfYjA0uoxqCH7kKdzhQbRWVO8J6M+NZkxvPI7A4EJtgYFiRKEOjYO74BeW0UIj904Ms9NAYN6MnU28GjQ895q7AmIkyP/RO9z2yNU5Obnt4VZhJoLsWU+sfMFK0VdoPAoPK52EjeUq7gW3Bfd9ig2/V5dlcNPn55R5HY8Hs5lq6iTpH2rM2wr2s7q4VEfbLQZw7mHNm01btpH7MSuuxgHBJc7DcN9uxRYViDQw666TMjWXflJFzB3WA/NotrRbAH9KWTMISrtc9XunRjd+plBbUOyNPR','pineId':'STD;EMA','pineVersion':'29.0','pineFeatures':{'v':'{\'indicator\':1,\'plot\':1,\'ta\':1}','f':True,'t':'text'},'in_0':{'v':50,'f':True,'t':'integer'},'in_1':{'v':'close','f':True,'t':'source'},'in_2':{'v':0,'f':True,'t':'integer'},'in_3':{'v':'EMA','f':True,'t':'text'},'in_4':{'v':5,'f':True,'t':'integer'},'in_5':{'v':'','f':True,'t':'resolution'},'in_6':{'v':True,'f':True,'t':'bool'}}],
    'ema100': ['Script@tv-scripting-101!',{'text':'bmI9Ks46_YgiQhsSwDdbNYHsEzTaxnA==_tysyiC9xdsEwtdmdMBSVgXuVvcZQ9j6XhIppaillwsxzP5xbNHizoC2fq0d6Q6EZeh3JWFos4nGmxiOETJ4ncnF0L/i6laHxlvePKlj2JEbxW5NGFl5l2KgufioukfuvBYZK/wIWE/3hLrlxXITNc1MWs10LKta7PyhbyJ2gW6G8S+VU0P4L4JBVQurjsKg7vFM9IiSGgZ1MYb655UzYrm9q4VuIlFVj3wQsYj+xf2lK947wZETX1p8T3moRqYmpZ32GT6V5Krk2pVttLcUIAu1pzUOC6cw1f7PNI7dmOskToyk4TpxiVnqbZRRmj2N+vPdb/nXCSQOLH3fX3McEz6uguxb0MBQgnbCMrdV6bDtVB5xiCfYjA0uoxqCH7kKdzhQbRWVO8J6M+NZkxvPI7A4EJtgYFiRKEOjYO74BeW0UIj904Ms9NAYN6MnU28GjQ895q7AmIkyP/RO9z2yNU5Obnt4VZhJoLsWU+sfMFK0VdoPAoPK52EjeUq7gW3Bfd9ig2/V5dlcNPn55R5HY8Hs5lq6iTpH2rM2wr2s7q4VEfbLQZw7mHNm01btpH7MSuuxgHBJc7DcN9uxRYViDQw666TMjWXflJFzB3WA/NotrRbAH9KWTMISrtc9XunRjd+plBbUOyNPR','pineId':'STD;EMA','pineVersion':'29.0','pineFeatures':{'v':'{\'indicator\':1,\'plot\':1,\'ta\':1}','f':True,'t':'text'},'in_0':{'v':100,'f':True,'t':'integer'},'in_1':{'v':'close','f':True,'t':'source'},'in_2':{'v':0,'f':True,'t':'integer'},'in_3':{'v':'EMA','f':True,'t':'text'},'in_4':{'v':5,'f':True,'t':'integer'},'in_5':{'v':'','f':True,'t':'resolution'},'in_6':{'v':True,'f':True,'t':'bool'}}],
    'ema200': ['Script@tv-scripting-101!',{'text':'bmI9Ks46_YgiQhsSwDdbNYHsEzTaxnA==_tysyiC9xdsEwtdmdMBSVgXuVvcZQ9j6XhIppaillwsxzP5xbNHizoC2fq0d6Q6EZeh3JWFos4nGmxiOETJ4ncnF0L/i6laHxlvePKlj2JEbxW5NGFl5l2KgufioukfuvBYZK/wIWE/3hLrlxXITNc1MWs10LKta7PyhbyJ2gW6G8S+VU0P4L4JBVQurjsKg7vFM9IiSGgZ1MYb655UzYrm9q4VuIlFVj3wQsYj+xf2lK947wZETX1p8T3moRqYmpZ32GT6V5Krk2pVttLcUIAu1pzUOC6cw1f7PNI7dmOskToyk4TpxiVnqbZRRmj2N+vPdb/nXCSQOLH3fX3McEz6uguxb0MBQgnbCMrdV6bDtVB5xiCfYjA0uoxqCH7kKdzhQbRWVO8J6M+NZkxvPI7A4EJtgYFiRKEOjYO74BeW0UIj904Ms9NAYN6MnU28GjQ895q7AmIkyP/RO9z2yNU5Obnt4VZhJoLsWU+sfMFK0VdoPAoPK52EjeUq7gW3Bfd9ig2/V5dlcNPn55R5HY8Hs5lq6iTpH2rM2wr2s7q4VEfbLQZw7mHNm01btpH7MSuuxgHBJc7DcN9uxRYViDQw666TMjWXflJFzB3WA/NotrRbAH9KWTMISrtc9XunRjd+plBbUOyNPR','pineId':'STD;EMA','pineVersion':'29.0','pineFeatures':{'v':'{\'indicator\':1,\'plot\':1,\'ta\':1}','f':True,'t':'text'},'in_0':{'v':200,'f':True,'t':'integer'},'in_1':{'v':'close','f':True,'t':'source'},'in_2':{'v':0,'f':True,'t':'integer'},'in_3':{'v':'EMA','f':True,'t':'text'},'in_4':{'v':5,'f':True,'t':'integer'},'in_5':{'v':'','f':True,'t':'resolution'},'in_6':{'v':True,'f':True,'t':'bool'}}],
}


class TradingView:
    def __init__(self,
                 username = '',
                 password = '',
                 token = '',
                 market = '') -> None:
        self._username = username
        self._password = password
        self._market = market
        self._token = token

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def market(self) -> str:
        return self._market

    @property
    def token(self) -> str:
        if not self._token:
            self._token = _get_auth_token(self.username, self.password)
        return self._token

    def current_quote(self, symbol: str) -> dict:
        # create tunnel
        headers = json.dumps({'Origin': 'https://data.tradingview.com'})
        ws = create_connection(_WS_URL_, headers=headers)
        sess = _generate_session('qs_')

        # Send messages
        if self.token:
            _send_message(ws, 'set_auth_token', [self.token])
        else:
            _send_message(ws, 'set_auth_token', ['unauthorized_user_token'])

        _send_message(ws, 'quote_create_session', [sess])
        _send_message(ws, 'quote_set_fields', [sess, 'lp', 'ch', 'lp_time'])
        _send_message(ws, 'quote_add_symbols', [sess, symbol])

        quote = _socket_quote(ws)

        return quote

    def realtime_quote(self, symbols: List[str], callback):
        # create tunnel
        headers = json.dumps({'Origin': 'https://data.tradingview.com'})
        ws = create_connection(_WS_URL_, headers=headers)
        sess = _generate_session('qs_')

        # Send messages
        if self.token:
            _send_message(ws, 'set_auth_token', [self.token])
        else:
            _send_message(ws, 'set_auth_token', ['unauthorized_user_token'])

        _send_message(ws, 'quote_create_session', [sess])
        _send_message(ws, 'quote_set_fields', [sess, 'lp', 'ch', 'lp_time'])

        for i in symbols:
            _send_message(ws, 'quote_add_symbols', [sess, i])

        # Start job
        _socket_quote(ws, callback)

    def historical_charts(self, symbol: str, interval: str, total_candle: int, charts: List[str], adjustment='dividends') -> pd.DataFrame:
        from itertools import islice

        def batched(iterable, n):
            "Batch data into tuples of length n. The last batch may be shorter."
            # batched('ABCDEFG', 3) --> ABC DEF G
            if n < 1:
                raise ValueError('n must be at least one')
            it = iter(iterable)
            while (batch := tuple(islice(it, n))):
                yield batch

        df = pd.DataFrame()
        for i in batched(charts, 3):
            data = self.historical_charts_chunk(symbol=symbol, interval=interval, total_candle=total_candle, charts=i, adjustment='dividends')
            if df.empty:
                df = data
            else:
                df = pd.concat([df, data], axis=1).T.drop_duplicates().T

        if df.empty:
            df = self.historical_charts_chunk(symbol=symbol, interval=interval, total_candle=total_candle, charts=[], adjustment='dividends')

        df['timestamp_ts'] = df['timestamp_ts'].astype(int)
        df['volume'] = df['volume'].astype(int)

        return df

    def historical_charts_chunk(self, symbol: str, interval: str, total_candle: int, charts: List[str], adjustment='dividends') -> pd.DataFrame:
        # create tunnel
        headers = json.dumps({'Origin': 'https://data.tradingview.com'})
        ws = create_connection(_WS_URL_, headers=headers)
        sess = _generate_session('cs_')

        # Send messages
        if self.token:
            _send_message(ws, 'set_auth_token', [self.token])
        else:
            _send_message(ws, 'set_auth_token', ['unauthorized_user_token'])

        # Then send a message through the tunnel
        _send_message(ws, 'set_data_quality', ['high'])
        _send_message(ws, 'chart_create_session', [sess, ''])
        _send_message(ws, 'resolve_symbol', [sess, 'sds_sym_1', "={\"adjustment\":\"" + adjustment + "\",\"currency-id\":\"USD\",\"symbol\":\"" + symbol + "\"}"])
        _send_message(ws, 'create_series', [sess, 's_ohlcv', 's1', 'sds_sym_1', str(interval), total_candle, ""])

        for chart in charts:
            chart_setting = CHARTS_SETTINGS[chart]
            _send_message(ws, 'create_study', [sess, f's_{chart}','st1','s_ohlcv',*chart_setting])

        # Start job
        df = _parse_bar_charts(ws, interval, series_num=1 + len(charts))

        return df

    def historical_bar_chart(self, symbol: str, interval, total_candle, adjustment='dividends') -> pd.DataFrame:
        # create tunnel
        headers = json.dumps({'Origin': 'https://data.tradingview.com'})
        ws = create_connection(_WS_URL_, headers=headers)
        sess = _generate_session('cs_')

        # Send messages
        if self.token:
            _send_message(ws, 'set_auth_token', [self.token])
        else:
            _send_message(ws, 'set_auth_token', ['unauthorized_user_token'])

        # Then send a message through the tunnel
        _send_message(ws, 'set_data_quality', ['high'])
        _send_message(ws, 'set_auth_token', ['unauthorized_user_token'])
        _send_message(ws, 'chart_create_session', [sess, ''])
        _send_message(ws, 'resolve_symbol', [sess, 'symbol_1', '={"symbol":"' + symbol + '","adjustment":"' + adjustment + '","session":"regular"}'])
        _send_message(ws, 'create_series', [sess, 's1', 's1', 'symbol_1', str(interval), total_candle, ''])

        # Start job
        df = _socket_bar_chart(ws, interval)

        return df

    def get_symbol_id(self, pair: str, market: str = ''):
        data = self.search(pair, market)

        symbol_name = data['symbol']
        if data['type'] == 'futures':
            symbol_name = data['contracts'][0]['symbol']

        broker = data['exchange']
        symbol_id = f'{broker.upper()}:{symbol_name.upper()}'
        return symbol_id

    def search(self, query: str, market: str = ''):
        # type = 'stock' | 'futures' | 'forex' | 'cfd' | 'crypto' | 'index' | 'economic'
        # query = what you want to search!
        # it returns first matching item
        res = get(_API_URL_, params={
            'text': query,
            'type': market or self._market,
        }, timeout=60)
        if res.status_code == 200:
            res = res.json()
            assert len(res) != 0, 'Nothing Found.'
            return res[0]
        else:
            print('Network Error!')


def _get_auth_token(username, password):
    if not username or not password:
        return ''

    sign_in_url = 'https://www.tradingview.com/accounts/signin/'

    data = {'username': username, 'password': password, 'remember': 'on'}
    headers = {'Referer': 'https://www.tradingview.com'}
    resp = post(url=sign_in_url, data=data,
                headers=headers, timeout=60)
    import json
    auth_token = resp.json()['user']['auth_token']

    return auth_token


def _socket_quote(ws, callback=None):
    resp_cbs = {}

    while True:
        try:
            result = ws.recv()

            if 'session_id' in result:
                continue

            matches = re.findall('^.*?({.*)$', result)
            res = []
            for _m in matches:
                res += re.split('~m~\d+~m~', _m)

            for _r in res:
                if not _r or 'session_id' in _r or 'quote_completed' in _r:
                    continue

                resp = json.loads(_r)

                resp_cb = {}
                if resp['m'] == 'qsd':
                    n = resp['p'][1]['n']
                    lp = resp['p'][1]['v'].get('lp', 0.0)
                    ch = resp['p'][1]['v'].get('ch', 0.0)
                    ts = resp['p'][1]['v'].get('lp_time', 0)
                    resp_cb = resp_cbs.get(n, {'symbol': n})
                    if lp:
                        resp_cb.update({'price': lp})
                    if ch:
                        resp_cb.update({'change': ch})
                    if ts:
                        resp_cb.update({'timestamp_ts': ts})

                    resp_cbs.update({n: resp_cb})

                    if callback:
                        callback(resp_cb)
                    elif 'price' in resp_cb and 'timestamp_ts' in resp_cb:
                        return resp_cb

            if not res:
                # ping packet
                _send_ping_packet(ws, result)
        except KeyboardInterrupt:
            break
        except:
            continue


def _parse_bar_charts(ws, interval, series_num=1) -> pd.DataFrame:
    data = []
    series_all = {}

    while True:
        try:
            result = ws.recv()
            if not result or '"quote_completed"' in result or '"session_id"' in result:
                continue

            # TODO: fix this tech dept, when send ping packet not right way
            out = re.search('"s[_a-z0-9]*":\[(.+?)\}\]', result)
            if not out:
                continue
            # TODO: fix this tech dept, when send ping packet not right way
            out = out.group(1)
            items = out.split(',{\"')
            if len(items) == 0:
                _send_ping_packet(ws, interval, result)
                continue

            series = find_series(result)
            if not series:
                continue

            series_all.update(series)
            if len(series_all) < series_num:
                continue

            for k, v in series_all.items():
                for i, bar in enumerate(v):
                    if len(data) <= i:
                        data.append({})
                    if k == 's_ohlcv':
                        cols = ['timestamp_ts', 'open', 'high', 'low', 'close', 'volume']
                        data[i].update(dict(zip(cols, bar)))
                        if 'volume' not in data[i]:
                            data[i]['volume'] = 0
                    else:
                        cols = ['timestamp_ts', k.strip('s_')]
                        data[i].update(dict(zip(cols, bar)))

            df = pd.DataFrame(data)

            for i in df.columns:
                df[i] = df[i].astype(float)

            df['timestamp_ts'] = df['timestamp_ts'].astype(int)
            df['volume'] = df['volume'].astype(int)

            return df
        except KeyboardInterrupt:
            break
        except Exception as e:
            # break
            print("=========except", datetime.now(), e)
            if ('closed' in str(e) or 'lost' in str(e)):
                print("=========try")
                # self.realtime_bar_chart(5, 1, callback)


def _socket_bar_chart(ws, interval) -> pd.DataFrame:
    while True:
        try:
            result = ws.recv()
            if not result or '"quote_completed"' in result or '"session_id"' in result:
                continue

            out = re.search('"s":\[(.+?)\}\]', result)
            if not out:
                continue

            out = out.group(1)
            items = out.split(',{\"')
            if len(items) != 0:
                datas = []
                for item in items:
                    item = re.split('\[|:|,|\]', item)
                    s = {
                        'timestamp_ts': int(float(item[4])),
                        'open': float(item[5]),
                        'high': float(item[6]),
                        'low': float(item[7]),
                        'close': float(item[8]),
                        'volume': float(item[9] if item[9].replace('.', '').isnumeric() else 0.0),
                    }
                    datas.append(s)

                df = pd.DataFrame(datas)

                return df
            else:
                # ping packet
                print("................retry")
                _send_ping_packet(ws, interval, result)
        except KeyboardInterrupt:
            break
        except Exception as e:
            # break
            print("=========except", datetime.now(), e)
            if ('closed' in str(e) or 'lost' in str(e)):
                print("=========try")
                # self.realtime_bar_chart(5, 1, callback)


def _generate_session(prefix):
    string_length = 12
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(string_length))
    return prefix + random_string


def _prepend_header(st):
    return '~m~' + str(len(st)) + '~m~' + st


def _construct_message(func, params):
    return json.dumps({'m': func, 'p': params}, separators=(',', ':'))


def _create_message(func, params):
    return _prepend_header(_construct_message(func, params))


def _send_message(ws, func, args):
    ws.send(_create_message(func, args))


def _send_ping_packet(ws, result):
    ping_str = re.findall('.......(.*)', result)
    if len(ping_str) != 0:
        ping_str = ping_str[0]
        ws.send('~m~' + str(len(ping_str)) + '~m~' + ping_str)


def find_series(string: str) -> Dict[str, List[dict]]:
    prefix_pattern = '{"s[_a-z0-9]*":\{"node":"'
    prefix_slice = slice(2, -11) # 2: {" AND -11: ":{"node":"

    series_ls = find_series_list(prefix_pattern, string)
    prefixes = find_series_prefixes(prefix_pattern, string, prefix_slice)

    series = dict(zip(prefixes, series_ls))

    return series

def find_series_list(pattern: str, string: str) -> List[dict]:
    '''
    Find series-liked postfix from a big raw string.
    '''
    series_ls = []
    for i in re.split(f'{pattern}', string):
        match = re.search('\[{"i":.*?}\]', i)
        if not match:
            continue

        bar_ls = json.loads(i[slice(*match.span())])
        bar_filter = filter(lambda x: x.get('i') > 0, bar_ls)
        bar_sorted = sorted(bar_filter, key=lambda x: x.get('i'))
        bar_values = map(lambda x: x.get('v'), bar_sorted)

        series_ls.append(list(bar_values))

    return series_ls

def find_series_prefixes(pattern: str, string: str, s: slice) -> List[str]:
    '''
    Find series-liked prefixes from a big raw string.
    '''
    prefixes = [i.group()[s] for i in re.finditer(f'{pattern}', string)]
    return prefixes

def set_index_by_timestamp(df: pd.DataFrame) -> pd.DataFrame:
    df['timestamp_ts'] = df['timestamp_ts'].astype(int)
    df['timestamp'] = pd.to_datetime(df['timestamp_ts'], unit='s').dt.tz_localize('UTC').dt.tz_convert(TZ_CST) # TODO: shift time to market close
    df.set_index('timestamp', drop=True, inplace=True)
    return df