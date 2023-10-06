from os import environ
from subprocess import check_call

from setuptools import find_packages, setup
from setuptools.command.install import install

GIT_SSH_KEY = environ.get('GIT_SSH_KEY', '')


class PostInstallCommand(install):
    '''Post-installation for installation mode.'''

    def run(self):
        check_call('python install.py --force'.split())
        install.run(self)


setup(
    name='zipline_bundles',
    cmdclass={
        'install': PostInstallCommand,
    },
    version='0.1',
    packages=['.', 'zipline-bundles'],
    entry_points={
        'console_scripts': ['zipline-bundles-install=install:main'],
    },
    install_requires=[
        'iexfinance',
        'logbook',
        'python-binance',
        'yahoofinancials',
        f'py-datasource @ git+https://${GIT_SSH_KEY}@github.com/TsevenSG/py-datasource.git',
    ]
)
