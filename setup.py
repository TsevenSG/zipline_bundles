from os import environ

from setuptools import find_packages, setup

GIT_SSH_KEY = environ.get('GIT_SSH_KEY', '')


setup(
    name='zipline_bundles',
    version='0.1',
    packages=['zipline_ingest'],
    package_dir={
        'zipline_ingest': 'zipline_ingest',
    },
    entry_points={
        'console_scripts': ['zipline_ingest-install=install:main'],
    },
    install_requires=[
        'iexfinance',
        'logbook',
        'python-binance',
        'yahoofinancials',
        f'py-datasource @ git+https://${GIT_SSH_KEY}@github.com/TsevenSG/py-datasource.git',
    ]
)
