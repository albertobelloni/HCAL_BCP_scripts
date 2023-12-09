#!/usr/bin/python3

################################################################################
#usage: analyze_rxdata.py [-h] [--input_dir INPUT_DIR] [--output_dir OUTPUT_DIR]
#
#optional arguments:
#  -h, --help            show this help message and exit
#  --input_dir INPUT_DIR
#           input directory (default: /afs/cern.ch/user/a/abelloni/BCAL/DATA
#  --output_dir OUTPUT_DIR
#           output directory (default: /afs/cern.ch/user/a/abelloni/BCAL/RESULTS
#
# The script will look for keys in the header of the input file that end with
# "[15:0]", and interpret them as the RX data of interest
################################################################################

from os import listdir,path
import argparse

from IlaData import IlaData

def parsed_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir",
			help="input directory "\
			"(default: %(default)s)",
			default="/afs/cern.ch/user/a/abelloni/BCAL/DATA")
    parser.add_argument("--output_dir",
			help="output directory "\
			"(default: %(default)s)",
			default="/afs/cern.ch/user/a/abelloni/BCAL/RESULTS")
    return parser.parse_args()

def main(args):
    
    # loop over files in the data directory
    # Rather complex lambda function to add full path in front of file name
    for data_file in [path.join(args.input_dir, file) \
		      for file in listdir(args.input_dir)]:
        # print update to terminal
        print (f"Analyzing: {data_file}")
        # create an IlaData object for the file
        analyzer = IlaData(data_file, args.output_dir)
        # run the analysis
        analyzer.full_analyze()

if __name__ == "__main__":

    args = parsed_args()
    try:
        main(args)
    except KeyboardInterrupt:
        pass
    
