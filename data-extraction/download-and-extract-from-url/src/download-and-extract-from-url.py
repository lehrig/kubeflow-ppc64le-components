import argparse
import logging
import os
from subprocess import run
import sys
import tarfile
import zipfile

def get_arg_parser():
    parser = argparse.ArgumentParser(description='Kubeflow download and extraction (zip/tar/tar.gz) component')
    parser.add_argument('--url', type=str,
                        default=None,
                        help='Url from which data has to be downloaded.')
    parser.add_argument('--fileName', type=str,
                        default="data.zip",
                        help='Name of the file to be stored.')
    parser.add_argument('--dataPath', type=str,
                        default="data",
                        help='Name of the folder that data is extrated to.')

    return parser


def main(args):
logging.basicConfig(format=FORMAT)
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format='%(asctime)s;%(levelname)s;%(message)s'
    )
    
    logging.info("Downloading from URL: " + args.url)
    
    file = args.fileName
    logging.info("Downloading to persistent volume: " + file + "...")
    run(['wget', args.url, '-O', file], capture_output=True)
    logging.info("Downloaded to " + file)

    logging.info("Extracting to '" + args.dataPath + "'...")
    if file.endswith("zip"):
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(args.dataPath)
    elif file.endswith("tar.gz"):
        with tarfile.open(file, "r:gz") as tar_gz_ref:
            tar_gz_ref.extractall(args.dataPath)
    elif file.endswith("tar"):
        with tarfile.open(file, "r:") as tar_ref:
            tari_ref.extractall(args.dataPath)

    logging.info("Result:")
    logging.info(os.listdir(args.dataPath))

    logging.info("Removing '" + file + "' again...")
    if os.path.isfile(file):
        os.remove(file)
    else:
        logging.error("Error: file '" + file + "' not found!")

    logging.info("Finished.")

if __name__ == "__main__":
    parser = get_arg_parser()
    args = parser.parse_args()
    main(args)

