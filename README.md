A little script designed to unpack and analyze CMS HB data received in an ILA.
The (vast) majority of the code was written by Joseph Mariano:
https://github.com/jmariano-cern/HcalBcpIlaAnalyzer

```
usage: analyze_rxdata.py [-h] [-i INPUT_DIR] [-o OUTPUT_DIR] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_DIR, --input_dir INPUT_DIR
           input directory (default: /afs/cern.ch/user/a/abelloni/BCAL/DATA
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
           output directory (default: /afs/cern.ch/user/a/abelloni/BCAL/RESULTS
  -v, --verbose         verbosity (default: not verbose)
```

The script will look for keys in the header of the input file that end with "[15:0]", and interpret them as the RX data of interest.

Caveats: the key name must NOT contain the character "/", as it is used to create a directory where the analysis results are stored. 

For more details and usage instructions see
    https://twiki.cern.ch/twiki/bin/view/Main/HcalBcp512#Data_Analysis
