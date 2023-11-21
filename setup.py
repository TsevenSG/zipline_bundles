from os import environ

from setuptools import find_packages, setup

GIT_SSH_KEY = environ.get('GIT_SSH_KEY', '')


setup(
    name='zipline_bundles',
    version='1.0.0',
    packages=['zipline.bundles.ingest'],
    package_dir={
        'zipline.bundles.ingest': 'ingest',
    },
    entry_points={
        'console_scripts': ['zipline-bundles-ingest-install=zipline.bundles.ingest.install:main'],
    },
    install_requires=[
        'iexfinance',
        'logbook',
        'python-binance',
        'yahoofinancials',
        f'py-datasource @ git+https://${GIT_SSH_KEY}@github.com/TsevenSG/py-datasource.git@1.0.2',
    ]
)
