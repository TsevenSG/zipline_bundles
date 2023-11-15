#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from zipline.data.bundles import register
from zipline.data.bundles.ingester import csv_ingester # ingester.py need to be placed in zipline.data.bundles

_DEFAULT_PATH = str(Path.home() / '.zipline/csv/yahoo')

# https://github.com/quantopian/trading_calendars

register(
    'yahoo_csv',
    csv_ingester('YAHOO',
                 every_min_bar=False, # the price is daily
                 csvdir_env='YAHOO_CSVDIR',
                 csvdir=_DEFAULT_PATH,
                 index_column='Date',
                 column_mapper={'Open': 'open',
                                'High': 'high',
                                'Low': 'low',
                                'Close': 'close',
                                'Volume': 'volume',
                                'Adj Close': 'price',
                 },
    ),
    calendar_name='NYSE',
)

from zipline.data.bundles.ingester import direct_ingester

from zipline.data.bundles import yahoo
register('yahoo_direct', # bundle's name
         direct_ingester('YAHOO',
                         every_min_bar=False,
                         symbol_list_env='SYMS', # the environment variable holding the comma separated list of assert names
                         downloader=yahoo.get_downloader(start_date='2010-01-01',
                                                         end_date='2020-01-01'
                         ),
         ),
         calendar_name='NYSE',
)

from zipline.data.bundles import tradingview
register('tv_64_stocks', # bundle's name
         direct_ingester('TRADINGVIEW',
                         every_min_bar=False,
                         symbol_list_env='SYMS', # the environment variable holding the comma separated list of assert names
                         downloader=tradingview.get_downloader(start_date='1990-01-01',
                                                               end_date='2024-01-01'
                         ),
         ),
         calendar_name='NYSE',
)

from zipline.data.bundles import tradingview
register('tv_latin_america', # bundle's name
         direct_ingester('TRADINGVIEW',
                         every_min_bar=False,
                         symbol_list_env='SYMS', # the environment variable holding the comma separated list of assert names
                         downloader=tradingview.get_downloader(start_date='1990-01-01',
                                                               end_date='2024-01-01'
                         ),
         ),
         calendar_name='NYSE',
)

from zipline.data.bundles import tradingview
register('tv_treasury', # bundle's name
         direct_ingester('TRADINGVIEW',
                         every_min_bar=False,
                         symbol_list_env='SYMS', # the environment variable holding the comma separated list of assert names
                         downloader=tradingview.get_downloader(start_date='1990-01-01',
                                                               end_date='2024-01-01'
                         ),
         ),
         calendar_name='NYSE',
)

from zipline.data.bundles import tradingview
register('tv_custom', # bundle's name
         direct_ingester('TRADINGVIEW',
                         every_min_bar=False,
                         symbol_list_env='SYMS', # the environment variable holding the comma separated list of assert names
                         downloader=tradingview.get_downloader(start_date='1990-01-01',
                                                               end_date='2024-01-01'
                         ),
         ),
         calendar_name='NYSE',
)
