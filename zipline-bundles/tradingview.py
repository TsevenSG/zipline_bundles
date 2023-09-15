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
    'BIL': 'AMEX:BIL',
    'USO': 'AMEX:USO',
    'CPER': 'AMEX:CPER',
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
    'QQQE': [
        '2012-05-31',
        '2012-06-12',
        '2012-06-13',
        '2012-06-15',
        '2012-06-18',
        '2012-06-22',
        '2012-07-18',
        '2012-07-20',
        '2012-08-03',
        '2012-08-08',
        '2012-08-15',
        '2012-08-17',
        '2012-08-22',
        '2012-08-23',
        '2012-08-27',
        '2012-08-28',
        '2012-09-04',
        '2012-09-05',
        '2012-09-10',
        '2012-09-18',
        '2012-09-20',
        '2012-09-26',
        '2012-09-27',
        '2012-09-28',
        '2012-10-02',
        '2012-10-03',
        '2012-10-04',
        '2012-10-08',
        '2012-10-09',
        '2012-10-12',
        '2012-10-22',
        '2012-10-24',
        '2012-10-25',
        '2012-10-31',
        '2012-11-02',
        '2012-11-06',
        '2012-11-07',
        '2012-11-08',
        '2012-11-12',
        '2012-11-14',
        '2012-11-15',
        '2012-11-21',
        '2012-11-23',
        '2012-11-30',
        '2012-12-03',
        '2012-12-04',
        '2012-12-06',
        '2012-12-12',
        '2012-12-13',
        '2012-12-14',
        '2012-12-18',
        '2012-12-24',
        '2012-12-26',
        '2013-01-08',
        '2013-01-09',
        '2013-01-10',
        '2013-01-15',
        '2013-01-16',
        '2013-03-07',
        '2013-03-22',
        '2013-04-25',
        '2013-06-14',
        '2013-06-28',
        '2013-07-03',
        '2013-09-09',
        '2013-11-12',
        '2014-01-10',
        '2014-02-19',
    ],
    'VO': [
        '2004-06-16',
        '2004-06-29',
        '2004-07-13',
    ],
    'XLI': [
        '1999-01-26',
    ],
    'XLRE': [
        '2015-10-14',
        '2015-11-02',
        '2015-11-25',
        '2015-11-27',
        '2015-12-07',
        '2016-01-25',
        '2016-02-16',
    ],
    'EDV': [
        '2007-12-17',
        '2007-12-18',
        '2007-12-24',
        '2008-03-05',
        '2008-03-06',
        '2008-03-28',
        '2008-04-07',
        '2008-04-24',
        '2008-04-25',
        '2008-05-05',
        '2008-05-20',
        '2008-07-03',
        '2008-07-09',
        '2008-07-18',
        '2008-07-22',
        '2008-07-29',
        '2008-07-31',
        '2008-08-01',
        '2008-08-05',
        '2008-08-06',
        '2008-08-08',
    ],
    'FALN': [
        '2016-07-06',
        '2016-07-18',
        '2016-07-25',
        '2016-07-26',
        '2016-08-17',
        '2016-08-18',
        '2016-08-24',
        '2016-09-14',
        '2016-09-16',
        '2016-09-19',
        '2016-09-20',
        '2016-09-29',
        '2016-10-04',
        '2016-10-07',
        '2016-10-10',
        '2016-10-11',
        '2016-10-20',
        '2016-11-04',
        '2016-11-15',
        '2016-11-17',
        '2016-11-18',
        '2016-11-25',
        '2016-12-01',
        '2016-12-09',
        '2016-12-12',
        '2016-12-13',
        '2016-12-15',
        '2016-12-19',
        '2016-12-20',
        '2016-12-27',
        '2017-01-31',
        '2017-02-02',
        '2017-02-21',
        '2017-03-24',
        '2017-03-29',
        '2017-05-18',
        '2017-05-19',
    ],
    'EMB': [
        '2008-02-20',
    ],
    'EZU': [
        '2000-08-14',
        '2000-09-01',
        '2000-09-15',
        '2000-11-16',
    ],
    'EWI': [
        '1996-04-01',
        '1996-04-03',
        '1996-07-19',
        '1996-12-18',
        '1997-04-07',
        '1997-04-25',
        '1997-04-28',
        '1997-08-20',
        '1997-08-22',
        '2000-08-04',
        '2001-08-06',
        '2001-09-04',
        '2001-12-24',
        '2002-02-07',
        '2002-08-12',
        '2002-11-19',
        '2002-11-29',
        '2002-12-10',
        '2002-12-13',
        '2003-02-18',
        '2003-04-04',
        '2003-05-08',
        '2003-08-07',
        '2003-10-29',
        '2003-11-28',
        '2004-05-14',
        '2004-05-20',
    ],
    'EWP': [
        '1996-03-22',
        '1996-03-25',
        '1996-04-04',
        '1996-04-10',
        '1996-04-17',
        '1996-04-18',
        '1996-05-01',
        '1996-05-13',
        '1996-05-15',
        '1996-05-23',
        '1996-06-04',
        '1996-06-07',
        '1996-06-10',
        '1996-06-13',
        '1996-06-14',
        '1996-06-18',
        '1996-07-02',
        '1996-07-19',
        '1996-07-23',
        '1996-07-25',
        '1996-08-05',
        '1996-08-06',
        '1996-08-07',
        '1996-08-08',
        '1996-08-09',
        '1996-08-12',
        '1996-08-16',
        '1996-08-19',
        '1996-08-23',
        '1996-08-26',
        '1996-08-27',
        '1996-09-05',
        '1996-09-12',
        '1996-09-16',
        '1996-09-24',
        '1996-09-27',
        '1996-10-03',
        '1996-10-07',
        '1996-10-09',
        '1996-10-10',
        '1996-10-15',
        '1996-10-17',
        '1996-10-29',
        '1996-11-01',
        '1996-11-13',
        '1996-11-15',
        '1996-11-21',
        '1996-12-04',
        '1996-12-05',
        '1996-12-06',
        '1996-12-10',
        '1996-12-18',
        '1996-12-19',
        '1996-12-24',
        '1997-01-17',
        '1997-02-07',
        '1997-03-03',
        '1997-03-10',
        '1997-03-18',
        '1997-03-25',
        '1997-03-26',
        '1997-04-07',
        '1997-04-11',
        '1997-04-23',
        '1997-05-01',
        '1997-05-02',
        '1997-06-20',
        '1997-06-23',
        '1997-06-26',
        '1997-07-14',
        '1997-07-23',
        '1997-07-24',
        '1997-08-12',
        '1997-08-14',
        '1997-08-28',
        '1997-09-23',
        '1997-09-26',
        '1997-10-13',
        '1997-11-13',
        '1997-12-29',
        '2000-08-10',
        '2000-10-06',
        '2001-06-08',
        '2001-07-03',
        '2001-10-03',
        '2001-10-19',
        '2001-11-02',
        '2001-11-15',
        '2001-11-29',
        '2001-12-24',
        '2002-01-25',
        '2002-04-03',
        '2002-04-11',
        '2002-05-31',
        '2002-07-05',
        '2002-08-12',
        '2002-08-16',
        '2002-08-19',
        '2002-09-11',
        '2002-09-13',
        '2002-10-09',
        '2002-10-17',
        '2002-10-21',
        '2002-10-29',
        '2002-10-30',
        '2002-11-29',
        '2002-12-26',
        '2003-01-03',
        '2003-02-05',
        '2003-10-29',
    ],
    'EWQ': [
        '1996-03-22',
        '1996-03-25',
        '1996-04-01',
        '1996-04-08',
        '1996-04-16',
        '1996-06-05',
        '1996-06-06',
        '1996-06-07',
        '1996-06-10',
        '1996-06-12',
        '1996-06-13',
        '1996-06-19',
        '1996-07-01',
        '1996-07-09',
        '1996-07-19',
        '1996-08-13',
        '1996-08-23',
        '1996-09-20',
        '1996-10-04',
        '1996-12-10',
        '1997-01-21',
        '1997-04-10',
        '1997-04-11',
        '1997-05-07',
        '1997-08-20',
        '1998-01-23',
        '1998-02-24',
    ],
    'EWG': [
        '1996-03-20',
        '1996-03-21',
        '1996-06-11',
        '1996-06-13',
        '1996-06-14',
        '1996-07-10',
        '1996-08-08',
        '1997-03-19',
        '1997-04-22',
    ],
    'EZA': [
        '2003-02-11',
        '2003-02-12',
        '2003-02-14',
        '2003-02-26',
        '2003-02-27',
        '2003-02-28',
        '2003-03-03',
        '2003-03-04',
        '2003-03-05',
        '2003-03-06',
        '2003-03-11',
        '2003-03-14',
        '2003-03-19',
        '2003-03-21',
        '2003-03-24',
        '2003-03-25',
        '2003-03-31',
        '2003-04-01',
        '2003-04-02',
        '2003-04-03',
        '2003-04-08',
        '2003-04-10',
        '2003-04-17',
        '2003-04-23',
        '2003-04-24',
        '2003-04-29',
        '2003-05-16',
        '2003-05-20',
        '2003-05-23',
        '2003-06-03',
        '2003-06-05',
        '2003-07-16',
        '2003-08-07',
        '2003-10-02',
        '2004-02-26',
        '2004-06-18',
        '2004-06-23',
    ],
    'DXJ': [
        '2006-06-22',
        '2006-06-27',
        '2006-06-28',
        '2006-06-29',
        '2006-07-07',
        '2006-07-11',
        '2006-07-12',
        '2006-07-17',
        '2006-07-21',
        '2006-07-24',
        '2006-08-01',
        '2006-08-03',
        '2006-08-08',
        '2008-08-26',
        '2008-09-17',
        '2009-02-27',
        '2009-05-14',
        '2009-05-21',
        '2009-06-05',
        '2009-06-09',
        '2009-09-18',
        '2009-11-04',
        '2009-12-09',
        '2009-12-24',
    ],
    'ASHS': [
        '2016-12-08',
    ],
    'EWH': [
        '1996-04-24',
        '1996-08-07',
        '1996-08-09',
        '1996-08-12',
        '1996-09-27',
        '1996-11-04',
    ],
    'EWS': [
        '1996-03-21',
        '1996-07-03',
    ],
    'EIDO': [
        '2010-05-12',
        '2010-06-01',
        '2010-07-02',
    ],
    'EWM': [
        '1996-03-21',
        '1996-03-28',
        '1996-04-18',
        '1998-09-02',
        '2000-11-24',
    ],
    'KWEB': [
        '2013-08-05',
        '2013-08-09',
        '2013-08-19',
        '2013-08-27',
        '2013-08-30',
        '2013-09-03',
        '2013-09-17',
    ],
    'SCJ': [
        '2007-12-26',
        '2007-12-31',
        '2008-01-03',
        '2008-01-08',
        '2008-01-10',
        '2008-01-11',
        '2008-01-14',
        '2008-01-15',
        '2008-01-17',
        '2008-01-23',
        '2008-04-30',
        '2009-01-26',
        '2009-03-31',
        '2010-02-10',
        '2010-06-14',
        '2010-07-09',
        '2010-12-15',
        '2012-03-06',
        '2012-06-13',
        '2012-07-03',
        '2012-07-11',
        '2012-10-04',
        '2015-01-02',
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
    'EWC': [
        '1996-03-20',
        '1996-03-21',
        '1996-03-22',
        '1996-03-26',
        '1996-03-28',
        '1996-04-04',
        '1996-04-08',
        '1996-04-09',
        '1996-05-07',
        '1996-05-09',
        '1996-05-13',
        '1996-05-14',
        '1996-05-23',
        '1996-05-31',
        '1996-06-04',
        '1996-06-05',
        '1996-06-12',
        '1996-06-13',
        '1996-06-14',
        '1996-06-18',
        '1996-06-19',
        '1996-06-20',
        '1996-06-27',
        '1996-06-28',
        '1996-07-05',
        '1996-07-12',
        '1996-07-19',
        '1996-07-22',
        '1996-07-23',
        '1996-07-24',
        '1996-07-25',
        '1996-07-26',
        '1996-07-31',
        '1996-08-05',
        '1996-08-06',
        '1996-08-07',
        '1996-08-13',
        '1996-08-15',
        '1996-08-28',
        '1996-09-05',
        '1996-09-06',
        '1996-09-10',
        '1996-09-11',
        '1996-09-18',
        '1996-09-19',
        '1996-09-20',
        '1996-09-25',
        '1996-09-26',
        '1996-09-27',
        '1996-10-24',
        '1996-10-29',
        '1996-11-01',
        '1996-11-04',
        '1996-11-29',
        '1997-01-13',
        '1997-02-11',
        '1997-08-20',
        '1997-10-21',
        '1997-11-05',
        '1997-12-03',
        '1997-12-19',
        '1997-12-24',
        '1997-12-29',
        '1998-02-19',
        '1998-03-03',
        '1998-03-17',
        '1998-03-20',
        '1998-03-23',
        '1998-04-01',
        '1998-04-03',
        '1998-04-21',
        '1998-04-29',
        '1998-05-01',
        '1998-06-29',
        '1998-07-02',
        '1998-07-10',
        '1998-07-17',
        '1998-07-21',
        '1998-07-23',
        '1998-07-27',
        '1998-10-08',
        '1999-02-10',
        '1999-03-09',
        '1999-03-12',
        '1999-05-26',
        '1999-06-02',
        '1999-06-10',
        '1999-06-29',
        '1999-07-12',
        '1999-07-13',
        '1999-08-06',
        '1999-09-07',
        '1999-09-15',
        '1999-10-01',
        '1999-10-14',
        '1999-10-22',
        '1999-12-10',
        '1999-12-15',
        '2000-04-20',
        '2000-05-18',
        '2001-10-19',
        '2001-11-02',
        '2001-11-15',
        '2002-02-26',
    ],
    'CPER': [
        '2011-11-17',
        '2011-11-22',
        '2011-11-25',
        '2011-12-01',
        '2011-12-02',
        '2011-12-28',
        '2012-01-09',
        '2012-01-10',
        '2012-01-17',
        '2012-01-18',
        '2012-02-15',
        '2012-02-16',
        '2012-03-08',
        '2012-03-14',
        '2012-04-05',
        '2012-04-18',
        '2012-04-19',
        '2012-05-02',
        '2012-05-07',
        '2012-05-15',
        '2012-05-18',
        '2012-05-21',
        '2012-05-24',
        '2012-05-25',
        '2012-05-29',
        '2012-06-11',
        '2012-06-12',
        '2012-06-13',
        '2012-06-14',
        '2012-06-19',
        '2012-06-25',
        '2012-06-26',
        '2012-06-27',
        '2012-06-29',
        '2012-07-02',
        '2012-07-03',
        '2012-07-10',
        '2012-07-11',
        '2012-07-12',
        '2012-07-13',
        '2012-07-17',
        '2012-07-19',
        '2012-07-20',
        '2012-07-25',
        '2012-07-31',
        '2012-08-01',
        '2012-08-03',
        '2012-08-08',
        '2012-08-13',
        '2012-08-15',
        '2012-08-16',
        '2012-08-24',
        '2012-08-27',
        '2012-08-28',
        '2012-08-29',
        '2012-08-31',
        '2012-09-05',
        '2012-09-14',
        '2012-09-27',
        '2012-09-28',
        '2012-10-01',
        '2012-10-02',
        '2012-10-03',
        '2012-10-04',
        '2012-10-05',
        '2012-10-08',
        '2012-10-12',
        '2012-10-15',
        '2012-10-16',
        '2012-10-17',
        '2012-10-18',
        '2012-10-19',
        '2012-10-22',
        '2012-10-26',
        '2012-11-06',
        '2012-11-07',
        '2012-11-08',
        '2012-11-12',
        '2012-11-14',
        '2012-11-15',
        '2012-11-16',
        '2012-11-19',
        '2012-11-20',
        '2012-11-21',
        '2012-11-23',
        '2012-11-27',
        '2012-11-28',
        '2012-12-14',
        '2012-12-21',
        '2012-12-24',
        '2012-12-26',
        '2012-12-27',
        '2012-12-31',
        '2013-01-08',
        '2013-01-09',
        '2013-01-10',
        '2013-01-14',
        '2013-01-15',
        '2013-01-31',
        '2013-02-06',
        '2013-02-08',
        '2013-02-11',
        '2013-02-14',
        '2013-02-19',
        '2013-02-28',
        '2013-03-04',
        '2013-03-28',
        '2013-04-01',
        '2013-04-02',
        '2013-04-09',
        '2013-05-02',
        '2013-05-20',
        '2013-05-23',
        '2013-06-10',
        '2013-06-17',
        '2013-06-18',
        '2013-06-19',
        '2013-06-27',
        '2013-07-02',
        '2013-07-05',
        '2013-07-08',
        '2013-07-19',
        '2013-07-22',
        '2013-07-23',
        '2013-07-25',
        '2013-07-26',
        '2013-08-06',
        '2013-08-07',
        '2013-08-14',
        '2013-08-23',
        '2013-09-19',
        '2013-09-25',
        '2013-09-27',
        '2013-09-30',
        '2013-10-01',
        '2013-10-08',
        '2013-10-09',
        '2013-10-10',
        '2013-10-14',
        '2013-10-15',
        '2013-10-16',
        '2013-10-21',
        '2013-10-22',
        '2013-10-24',
        '2013-10-25',
        '2013-10-28',
        '2013-10-29',
        '2013-10-30',
        '2013-11-01',
        '2013-11-04',
        '2013-11-05',
        '2013-11-06',
        '2013-11-08',
        '2013-11-11',
        '2013-11-14',
        '2013-11-20',
        '2013-11-21',
        '2013-11-26',
        '2013-11-27',
        '2013-11-29',
        '2013-12-11',
        '2013-12-13',
        '2013-12-18',
        '2013-12-19',
        '2013-12-27',
        '2013-12-30',
        '2014-01-06',
        '2014-01-15',
        '2014-02-04',
        '2014-02-05',
        '2014-02-06',
        '2014-02-11',
        '2014-02-12',
        '2014-02-13',
        '2014-02-14',
        '2014-02-18',
        '2014-02-25',
        '2014-02-26',
        '2014-02-27',
        '2014-04-02',
        '2014-04-07',
        '2014-04-09',
        '2014-04-17',
        '2014-05-01',
        '2014-05-19',
        '2014-05-20',
        '2014-05-29',
        '2014-06-02',
        '2014-06-03',
        '2014-06-05',
        '2014-06-11',
        '2014-06-17',
        '2014-06-18',
        '2014-06-26',
        '2014-08-22',
        '2014-08-25',
        '2014-08-28',
        '2014-08-29',
        '2014-09-09',
        '2014-09-10',
        '2014-09-15',
        '2014-09-17',
        '2014-09-23',
        '2014-09-26',
        '2014-10-01',
        '2014-10-02',
        '2014-10-17',
        '2014-11-05',
        '2014-11-12',
        '2014-11-17',
        '2014-11-18',
        '2014-12-03',
        '2014-12-04',
        '2014-12-15',
        '2014-12-17',
        '2014-12-22',
        '2014-12-23',
        '2014-12-24',
        '2015-01-05',
        '2015-01-07',
        '2015-01-12',
        '2015-01-13',
        '2015-01-30',
        '2015-02-02',
        '2015-02-04',
        '2015-02-13',
        '2015-02-24',
        '2015-03-02',
        '2015-03-04',
        '2015-03-12',
        '2015-03-16',
        '2015-03-19',
        '2015-03-25',
        '2015-03-27',
        '2015-04-06',
        '2015-04-09',
        '2015-04-17',
        '2015-04-24',
        '2015-04-28',
        '2015-05-11',
        '2015-05-15',
        '2015-05-26',
        '2015-05-28',
        '2015-06-02',
        '2015-06-05',
        '2015-06-08',
        '2015-06-10',
        '2015-06-11',
        '2015-06-12',
        '2015-06-16',
        '2015-06-17',
        '2015-06-18',
        '2015-06-25',
        '2015-06-29',
        '2015-07-15',
        '2015-07-24',
        '2015-07-30',
        '2015-07-31',
        '2015-08-04',
        '2015-08-10',
        '2015-09-11',
        '2015-09-16',
        '2015-09-23',
        '2015-10-09',
        '2015-10-14',
        '2015-10-15',
        '2015-10-20',
        '2015-10-21',
        '2015-10-22',
        '2015-10-23',
        '2015-10-26',
        '2015-10-27',
        '2015-10-28',
        '2015-11-05',
        '2015-11-06',
        '2015-11-11',
        '2015-11-13',
        '2015-11-17',
        '2015-11-27',
        '2015-12-30',
        '2016-01-05',
        '2016-01-28',
        '2016-01-29',
        '2016-02-03',
        '2016-02-16',
        '2016-03-31',
        '2016-04-26',
        '2016-05-09',
        '2016-05-11',
        '2016-06-13',
        '2016-06-14',
        '2016-06-16',
        '2016-07-08',
        '2016-08-04',
        '2016-08-08',
        '2016-08-17',
        '2016-08-18',
        '2016-08-25',
        '2016-09-01',
        '2016-09-14',
        '2016-09-20',
        '2016-09-27',
        '2016-10-11',
        '2016-10-12',
        '2016-10-18',
        '2016-10-21',
        '2017-04-21',
        '2017-06-14',
        '2017-06-16',
        '2017-06-20',
        '2017-06-22',
        '2017-06-29',
        '2017-07-07',
        '2017-07-11',
        '2017-07-12',
        '2017-07-13',
        '2017-07-14',
        '2017-07-19',
        '2017-07-24',
        '2017-09-28',
        '2017-10-03',
        '2018-05-18',
        '2018-05-21',
        '2018-05-22',
        '2018-05-25',
        '2018-05-31',
        '2018-08-23',
    ],
    'UNL': [
        '2016-04-01',
        '2016-04-07',
        '2016-09-01',
        '2017-05-17',
        '2017-07-26',
        '2017-08-30',
        '2017-09-07',
        '2017-09-27',
        '2017-09-28',
        '2017-10-12',
        '2017-10-19',
        '2018-02-16',
        '2018-02-28',
        '2018-04-05',
        '2018-04-24',
        '2018-04-27',
        '2018-05-02',
        '2018-05-04',
        '2018-06-13',
        '2018-06-22',
        '2018-06-29',
        '2018-07-03',
        '2018-07-20',
        '2018-08-01',
        '2018-08-09',
        '2018-08-20',
        '2018-08-22',
        '2018-08-28',
        '2018-08-31',
        '2018-09-04',
        '2018-09-12',
        '2018-09-19',
    ],
    'WEAT': [
        '2011-11-15',
        '2012-01-24',
        '2012-02-02',
        '2012-03-13',
        '2012-05-01',
        '2012-06-07',
        '2012-11-23',
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

        print('\n', 'Downloading', symbol)

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