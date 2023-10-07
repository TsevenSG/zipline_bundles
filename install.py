import argparse
import logging
import shutil
import sys
from os import makedirs
from os.path import abspath, dirname, exists, expanduser, isdir, join


def copy(filelist, dest, src, force):
    for f in filelist:
        dstf=join(dest, f)
        if not force and exists(dstf):
            logging.error("'{}' already exists.".format(dstf))
            sys.exit(1)
        else:
            srcf=join(src, f)
            logging.info("copying '{}' to '{}'".format(srcf, dest))
            try:
                shutil.copyfile(srcf, dstf)
            except Exception as exp:
                logging.error("error while copying '{}' to '{}': {}".format(srcf, dest, exp))
                sys.exit(1)

def main(force=True):
    ### configure logging
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    # check if zipline is installed
    try:
        import zipline.data.bundles as bld
    except ImportError:
        logging.error('cannot found zipline. Run the installer in an environment where zipline is installed.')
        sys.exit(1)

    ### source files and directory
    src_dir=join(abspath(dirname(__file__)), 'zipline_ingest')
    src_ext=['extension.py']
    src_ing=['ingester.py', 'iex.py', 'tradingview.py', 'yahoo.py', 'binance.py']

    ### destination directories
    dst_ext=join(expanduser('~'), '.zipline')
    # check the existence of zipline home
    if not isdir(dst_ext):
        makedirs(dst_ext)
        # logging.error("zipline home ('{}') does not exist.")
        # sys.exit(1)

    dst_ing=bld.__path__[0]

    copy(src_ext, dst_ext, src_dir, force)
    copy(src_ing, dst_ing, src_dir, force)

if __name__ == "__main__":
    ### initialize the input argument parser
    parser=argparse.ArgumentParser(description='Add zipline bundles')
    parser.add_argument('-f', '--force', action='store_true', default=True)

    ### parse input arguments
    input_args=parser.parse_args()

    main(input_args.force)