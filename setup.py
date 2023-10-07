from os import environ

from setuptools import find_packages, setup

GIT_SSH_KEY = environ.get('GIT_SSH_KEY', '')


setup(
    name='zipline_bundles',
    version='0.1',
    packages=['ziplinebundles'],
    package_dir={
        'ziplinebundles': 'ziplinebundles',
    },
    # entry_points={
    #     'console_scripts': ['zipline-bundles-install=install:main'],
    # },
    install_requires=[
        'iexfinance',
        'logbook',
        'python-binance',
        'yahoofinancials',
        f'py-datasource @ git+https://${GIT_SSH_KEY}@github.com/TsevenSG/py-datasource.git',
    ]
)
