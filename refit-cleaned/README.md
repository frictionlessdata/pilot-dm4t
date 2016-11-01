# REFIT: Electrical Load Measurements (Cleaned)

This folder contains a very simple example of a Data Package derived from the cleaned [REFIT Electrical Load Measurements database](https://pure.strath.ac.uk/portal/en/datasets/refit-electrical-load-measurements-cleaned(9ab14b0e-19ac-4279-938f-27f643078cec.html).

- `Makefile`: A simple script that downloads the source [zipped dataset](https://pure.strath.ac.uk/portal/files/52873459/Processed_Data_CSV.7z) into a folder called `archive/` and unzips into a folder called `data/`. 
- `create_datapackage.ipynb`: This Jupyter notebook uses `metadata.yml` to create a basic Data Package on disk of the downloaded files.  `metadata.yml` was created as a more machine-readable version of the [original source readme](https://pure.strath.ac.uk/portal/files/52873458/REFIT_Readme.txt)
- `datapackage.json`: The Data Package descriptor file (see <http://specs.frictionlessdata.io/data-packages/> for details)
- `example.R`: Example R script using the [datapkg](https://github.com/ropenscilabs/datapkg) library.  [datapkg](https://github.com/ropenscilabs/datapkg) uses the `datapackage.json` to load the data and metadata into R
- `Rplots.pdf`: Output of `example.R`

## General Information

7zip required (`brew install p7zip` on Mac OS X)



