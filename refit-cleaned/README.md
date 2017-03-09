# REFIT: Electrical Load Measurements (Cleaned)

This folder contains a very simple example of a Data Package derived from the cleaned [REFIT Electrical Load Measurements database](https://pure.strath.ac.uk/portal/en/datasets/refit-electrical-load-measurements-cleaned(9ab14b0e-19ac-4279-938f-27f643078cec.html)).

- `Makefile`: A simple script that downloads the source [zipped dataset](https://pure.strath.ac.uk/portal/files/52873459/Processed_Data_CSV.7z) into a folder called `archive/` and unzips into a folder called `data/`.
- `create_datapackage.ipynb`: This Jupyter notebook uses `metadata.yml` to create a basic Data Package on disk of the downloaded files.  `metadata.yml` was created as a more machine-readable version of the [original source readme](https://pure.strath.ac.uk/portal/files/52873458/REFIT_Readme.txt)
- `datapackage.json`: The Data Package descriptor file (see <http://specs.frictionlessdata.io/data-packages/> for details)
- `example.R`: Example R script using the [datapkg](https://github.com/ropenscilabs/datapkg) library.  [datapkg](https://github.com/ropenscilabs/datapkg) uses the `datapackage.json` to load the data and metadata into R
- `Rplots.pdf`: Output of `example.R`

## General Information

7zip required (`brew install p7zip` on Mac OS X)

## Data Preview

```
$ head data/House_1.csv
Time,Unix,Aggregate,Appliance1,Appliance2,Appliance3,Appliance4,Appliance5,Appliance6,Appliance7,Appliance8,Appliance9
2013-10-09 13:06:17,1381323977,523,74,0,69,0,0,0,0,0,1
2013-10-09 13:06:31,1381323991,526,75,0,69,0,0,0,0,0,1
2013-10-09 13:06:46,1381324006,540,74,0,68,0,0,0,0,0,1
2013-10-09 13:07:01,1381324021,532,74,0,68,0,0,0,0,0,1
2013-10-09 13:07:15,1381324035,540,74,0,69,0,0,0,0,0,1
2013-10-09 13:07:18,1381324038,539,74,0,69,0,0,0,0,0,1
2013-10-09 13:07:30,1381324050,537,74,0,69,0,0,0,0,0,1
2013-10-09 13:07:32,1381324052,537,74,0,69,0,0,0,0,0,1
2013-10-09 13:07:44,1381324064,548,74,0,69,0,0,0,0,0,1
```

## Hosted Data Package

The data for this Data Package is too large (6.7GB) to be stored on
GitHub directly.  The full package has been uploaded to Amazon S3 for
loading directly into your tool of choice.

[datapackage.json](https://s3-eu-west-1.amazonaws.com/frictionlessdata.io/pilots/pilot-dm4t/datapackage.json)

[data.okfn.org view](http://data.okfn.org/tools/view?url=https%3A%2F%2Fs3-eu-west-1.amazonaws.com%2Ffrictionlessdata.io%2Fpilots%2Fpilot-dm4t%2Fdatapackage.json)

### Loading in R

```
library(datapkg)

refit <- datapkg_read('https://s3-eu-west-1.amazonaws.com/frictionlessdata.io/pilots/pilot-dm4t/datapackage.json')
```
