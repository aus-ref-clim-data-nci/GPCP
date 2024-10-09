#!/bin/bash
# Copyright 2021 ARC Centre of Excellence for Climate Extremes
#
# author: Sam Green <sam.green@unsw.edu.au>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
#This script is to concatenate the daily gpcp data into yearly files.
#
#Date created: 07-05-2024

# Initialize variables
yr=""
ver=""
freq=""
i=""

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -y) yr="$2"; shift ;;
        -v) ver="$2"; shift ;;
        -f) freq="$2"; shift ;;
        *) echo "Usage: $0 -y <year> -v <version> -f <frequency>"
           echo "<version> can be 1-3, 2-3, or 3-2"
           echo "<frequency> can be day or mon"
           exit 1 ;;
    esac
    shift
done

# Check if all required arguments are provided
if [[ -z "$yr" || -z "$ver" || -z "$freq" ]]; then
    echo "Usage: $0 -y <year> -v <version> -f <frequency>"
    echo "<version> can be 1-3, 2-3, or 3-2"
    echo "<frequency> can be day or mon"
    exit 1
fi

# Output the values
echo "The year is $yr"
echo "The version is $ver"
echo "The frequency is $freq"


root_dir="/g/data/jt48/aus-ref-clim-data-nci/gpcp/data/$freq/v$ver/tmp/$yr/"
outdir="/g/data/jt48/aus-ref-clim-data-nci/gpcp/data/$freq/v$ver/"

if [ -d "$outdir" ]; then
    echo "Directory $outdir exists."
else
    echo "Directory $outdir does not exist. Creating now..."
    mkdir -p "$outdir" || { echo "Failed to create directory $outdir" >&2; exit 1; }
fi

f_in=$root_dir/*$yr*.nc*
f_out=$outdir/gpcp_v${ver}_${freq}_${yr}.nc

echo "Concatenating $yr"

if [ -f "$f_out" ]; then
    echo "$f_out exists already, deleting"
    rm $f_out
else
    echo "File doesn't exist, proceeding"
fi

if [[ "$freq" == "mon" ]]; then
    i=12
else
    i=31  # or some other default value if freq is not "mon"
fi


# Concatenate all files from a day together, save as a tmp.nc file
cdo --silent --no_history -L -s -f nc4c -z zip_4 cat $f_in $outdir/tmp.nc
# Re-chunk the tmp.nc file
echo "Concatenating complete, now re-chunking...."
ncks --cnk_dmn time,$i --cnk_dmn lat,600 --cnk_dmn lon,600 $outdir/tmp.nc $f_out
#ncks --cnk_dmn time,31 --cnk_dmn lat,600 --cnk_dmn lon,600 $outdir/tmp.nc $f_out
rm $outdir/tmp.nc
# rewrite history attribute
hist="downloaded original files from 
    https://measures.gesdisc.eosdis.nasa.gov/data/GPCP/GPCPMON.2.3/
    Using cdo to concatenate files, and nco to modify chunks: 
    cdo --silent --no_warnings --no_history -L -s -f nc4c -z zip_4 cat $f_in $outdir/tmp.nc
    ncks --cnk_dmn time,$i --cnk_dmn lat,600 --cnk_dmn lon,600 tmp.nc $f_out"
# Add what we've done into the history attribute in the file. 
ncatted -h -O -a history,global,o,c,"$hist" ${f_out}
