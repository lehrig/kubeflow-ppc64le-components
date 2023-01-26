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
                        help='Name of the folder that data is extracted to.')

    return parser


def main(args):
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format='%(levelname)s %(asctime)s: %(message)s'
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
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tar_gz_ref, args.dataPath)
    elif file.endswith("tar"):
        with tarfile.open(file, "r:") as tar_ref:
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tari_ref, args.dataPath)

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

