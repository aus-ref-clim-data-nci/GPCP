# GPCP

![workflow](https://github.com/aus-ref-clim-data-nci/GPCP/actions/workflows/gpcp.yml/badge.svg)

## Overview

The Global Precipitation Climatology Project (GPCP),
produced by the NASA Mesoscale Atmospheric Processes Laboratory,
comprises threee products: one-degree daily (1DD), monthly product and pentad data.

We have downloaded the following products:
- daily v1.3: this is available up to a three months from present date and it is the recommended daily version.
- daily v3.2: this is the latest version but currently only has time range 06/2000 - 09/2021.
- monthly v2.3: which is the recommended monthly version, goes up to present date, contains some preliminary files.
- monthly v3.2: this is the latest version but currently only goes up to 1983 - 2023.

The GPCP One-Degree Daily Precipitation Data Set (1DD Data Set) provides daily,
global 1x1-deg gridded fields of precipitation totals for October 1996 through the delayed present.
The 1DD draws upon several different data sources, surface and satellite measurements, covering different areas of the globe.
This product is updated sporadically, about once a month.

More information is available from the [GPCP webpage](https://precip.gsfc.nasa.gov).
Detailed documentation is also available from the NCEI data server for
[v1.3 daily](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/doc/), [v3.2 daily](https://disc.gsfc.nasa.gov/datasets/GPCPDAY_3.2/summary?keywords=GPCPDAY),  [v2.3 monthly](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-monthly/doc/), and [v3.2 monthly](https://disc.gsfc.nasa.gov/datasets/GPCPMON_3.2/summary?keywords=GPCPMON).
These documents are also available on the filesystem in the dataset folder.

## Data download

We downloaded v1.3 daily and v2-3 monthly from the
[NCEI server](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/), using a python based code. The v3.2 daily and monthly was downloaded using wget from [GES DISC](https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/)
The code uses the requests module to download the files.

To run it:
```
python gpcp.py -y <year> -t <frequency>
```
To see all the options:
```
python gpcp.py --help
```

Weekly updates are managed via the [GitHub Action](https://github.com/aus-ref-clim-data-nci/GPCP/actions/workflows/gpcp.yml).


## Data location

We've downloaded GPCP data to:

```
/g/data/ia39/aus-ref-clim-data-nci/gpcp/data/<frequency>/<version>/<files>
```
where `<frequency>` is `mon` or `day` and
`<version>` is `v1-2`,`v3-2` for daily data and `v2-3`, `v3-2` for monthly.

Files are in netcdf4 format and have been concatenated into yearly files:
- v1.3 daily: gpcp_v1-3_day_YYYY.nc
- v3.2 daily: gpcp_L3_V3.2_day_YYYY.nc
- v2.3 monthly: gpcp_v2-3_mon_YYYY.nc
- v3.2 monthly: gpcp_L3_V3.2_mon_YYYY.nc

If preliminary files are present (currently applies only to v2.3 monthly)
then this is indicated in the filenames as in this example:
```
gpcp_v02r03-preliminary_monthly_d201908_c20190910.nc
```

## License

Unknown.

## Data citation

v1.3 daily - Adler, Robert; Wang, Jian-Jian; Sapiano, Mathew; Huffman, George; Bolvin, David; Nelkin, Eric; and NOAA CDR Program (2017). Global Precipitation Climatology Project (GPCP) Climate Data Record (CDR), Version 1.3 (Daily) [Indicate subset used.]. NOAA National Centers for Environmental Information. doi:10.7289/V5RX998Z [access date]

v3.2 daily - Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin (2022), GPCP Version 3.2 Daily Precipitation Data Set, Edited by Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin, Greenbelt, Maryland, USA, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: [Data Access Date], 10.5067/MEASURES/GPCP/DATA305

v2.3 monthly - Adler, Robert; Wang, Jian-Jian; Sapiano, Matthew; Huffman, George; Chiu, Long; Xie, Ping Ping; Ferraro, Ralph; Schneider, Udo; Becker, Andreas; Bolvin, David; Nelkin, Eric; Gu, Guojun; and NOAA CDR Program (2016). Global Precipitation Climatology Project (GPCP) Climate Data Record (CDR), Version 2.3 (Monthly). National Centers for Environmental Information. doi:10.7289/V56971M6 [access date]

v3.2 monthly - Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin (2022), GPCP Version 3.2 Satellite-Gauge (SG) Combined Precipitation Data Set, Edited by Huffman, G.J., A. Behrangi, D.T. Bolvin, E.J. Nelkin, Greenbelt, Maryland, USA, Goddard Earth Sciences Data and Information Services Center (GES DISC), Accessed: [Data Access Date], 10.5067/MEASURES/GPCP/DATA304


## Reference

Publications using this dataset should also cite the following journal article: 

Huffman GJ, Adler RF, Morrissey MM, Bolvin DT, Curtis S, Joyce R, McGavock B, and Susskind J (2001).
Global precipitation at one-degree daily resolution from multisatellite observations.
*Journal of Hydrometeorolgy*, 2, 36-50.
[https://doi.org/10.1175/1525-7541(2001)002<0036:GPAODD>2.0.CO;2](https://doi.org/10.1175/1525-7541(2001)002<0036:GPAODD>2.0.CO;2)

Huffman, George J., Adler, R. F., Behrangi, Ali, Bolvin, David T., Nelkin, Eric, Song, Yang. 2020.  Algorithm Theoretical Basis Document (ATBD) for Global Precipitation Climatology Project Version 3.1 Precipitation Data. URL: https://docserver.gesdisc.eosdis.nasa.gov/public/project/MEaSUREs/GPCP/GPCP_ATBD_V3.1.pdf

## Acknowledgement

No statement provided.

## Author note

Users are requested to add the official data citation as above and email their citation to
george.j.huffman@nasa.gov or david.t.bolvin@nasa.gov.

## Assistance

For assistance with GPCP data on NCI, open a new issue at https://github.com/aus-ref-clim-data-nci/GPCP/issues
