# GPCP

## Overview

The Global Precipitation Climatology Project (GPCP),
produced by the NASA Mesoscale Atmospheric Processes Laboratory,
comprises threee products: one-degree daily (1DD), monthly product and pentad data.

We have downloaded the following products:
- daily v1.2: this is limted to 2015 and currently not distributed anymore
- daily v1.3: this is available up to a three months from present date and it is the recommended daily version
- monthly v2.3: which is the recommended monthly version, goes up to present date, contains some preliminary files

The GPCP One-Degree Daily Precipitation Data Set (1DD Data Set) provides daily,
global 1x1-deg gridded fields of precipitation totals for October 1996 through the delayed present.
The 1DD draws upon several different data sources, surface and satellite measurements, covering different areas of the globe.
This product is updated sporadically, about once a month.

More information is available from the [GPCP webpage](https://precip.gsfc.nasa.gov).
Detailed documentation is also available from the NCEI data server for
[v1-3 daily](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/doc/) and
[v2.3 monthly](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-monthly/doc/).
These documents are also available on the filesystem in the dataset folder.

## Data download

We downloaded v1.3 daily and v2-3 monthly from the
[NCEI server](https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-daily/access/),
and v1.2 from the [NCAR Research Data Archive](https://rda.ucar.edu/datasets/ds728.3/#!description).

## Data location

We've downloaded GPCP data to:

```
/g/data/ia39/gpcp/<frequency>/<version>/<YYYY>/<files>
```
where `<frequency>` is `mon` or `day` and
`<version>` is `v1-2` and `v1-3` for daily data and `v2-3` for monthly.

Files are in netcdf4 format and filenames are respectively:
- `gpcp_1dd_v1.2_p1d.YYYYMMDD.nc` for v1.2 daily,
  where the date is the represented day,
  for example: `gpcp_1dd_v1.2_p1d.199610.nc`
- `gpcp_v01r03_daily_dYYYYMMDD_cYYYYMMDD.nc` for v1.3 daily,
  where the first date is the represented day and the second is the creation date for the file,
  for example: `gpcp_v01r03_daily_d20170323_c20171211.nc`
- `gpcp_v02r03_monthly_dYYYYMMDD_cYYYYMMDD.nc`, same conventions as for daily v1.3

If preliminary files are present (currently applies only to v2.3 monthly)
then this is indicated in the filenames as in this example:
```
gpcp_v02r03-preliminary_monthly_d201908_c20190910.nc
```

## License

Unknown.

## Data citation

v1.2: Huffman GJ, Bolvin DT, and Adler RF (2016).
GPCP Version 1.2 One-Degree Daily Precipitation Data Set.
*Research Data Archive at the National Center for Atmospheric Research, Computational and Information Systems Laboratory.*
https://doi.org/10.5065/D6D50K46. Accessed 30 Jan 2018.

v1.3: Unknown.

## Reference

Huffman GJ, Adler RF, Morrissey MM, Bolvin DT, Curtis S, Joyce R, McGavock B, and Susskind J (2001).
Global precipitation at one-degree daily resolution from multisatellite observations.
*Journal of Hydrometeorolgy*, 2, 36-50.
[https://doi.org/10.1175/1525-7541(2001)002<0036:GPAODD>2.0.CO;2](https://doi.org/10.1175/1525-7541(2001)002<0036:GPAODD>2.0.CO;2)

## Acknowledgement

No statement provided.

## Author note

Users are requested to add the official data citation as above and email their citation to
george.j.huffman@nasa.gov or david.t.bolvin@nasa.gov.
