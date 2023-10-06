import pandas as pd
from tradingview import (SYMBOLS_64_STOCKS, SYMBOLS_LATIN_AMERICA, TZ_CST,
                         TradingView)

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
