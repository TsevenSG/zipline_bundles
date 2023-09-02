import pandas as pd
import pytz

SYMBOLS = {
    'SPX': 'SP:SPX',
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
    # Latin America
    'EWZ': 'AMEX:EWZ',
    'EWW': 'AMEX:EWW',
    'ILF': 'AMEX:ILF',
    'IEF': 'NASDAQ:IEF',
    'TLT': 'NASDAQ:TLT',
    'CL1!': 'NYMEX:CL1!',
    'HG1!': 'COMEX:HG1!',
    'IRX.P': 'CBOE:IRX.P',
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

        df = tv.historical_bar_chart(symbol=SYMBOLS[symbol], interval='1D', total_candle=10000, adjustment='dividends')

        df['timestamp'] = pd.to_datetime(df['timestamp_ts'], unit='s').dt.tz_localize('UTC').dt.tz_convert(TZ_CST).dt.date
        df.set_index('timestamp', drop=True, inplace=True)
        df.drop('timestamp_ts', inplace=True, axis=1)

        df['dividend'] = 0
        df['split'] = 1

        print(df.head(3))

        return df

    return downloader


#@title Define TradingView class

import json
import random
import re
import string
from datetime import datetime
from enum import Enum
from typing import List

import pandas as pd
from requests import get, post
from websocket import create_connection

_GLOBAL_URL_ = 'https://scanner.tradingview.com/global/scan'
_API_URL_ = 'https://symbol-search.tradingview.com/symbol_search'
_WS_URL_ = 'wss://data.tradingview.com/socket.io/websocket'


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