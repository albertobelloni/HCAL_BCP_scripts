A little script designed to unpack and analyze CMS HB data received in an ILA.

```
Usage: analyze_rxdata.py [-h] [--input_dir INPUT_DIR] [--output_dir OUTPUT_DIR]

optional arguments:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
           input directory (default: /afs/cern.ch/user/a/abelloni/BCAL/DATA)
  --output_dir OUTPUT_DIR
           output directory (default: /afs/cern.ch/user/a/abelloni/BCAL/RESULTS)
```

The script will look for keys in the header of the input file that end with "[15:0]", and interpret them as the RX data of interest.

Caveats: the key name must NOT contain the character "/", as it is used to create a directory where the analysis results are stored. 

For more details and usage instructions see
    https://twiki.cern.ch/twiki/bin/view/Main/HcalBcp512#Data_Analysis
