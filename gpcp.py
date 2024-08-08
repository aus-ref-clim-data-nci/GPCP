#!/usr/bin/env python
"""
Copyright 2021 ARC Centre of Excellence for Climate Extremes 

author: Paola Petrelli <paola.petrelli@utas.edu.au>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This script is used to download, checksum and update the GPCP dataset on
 the NCI server
The dataset is stored in /g/data/ia39/aus-ref-clim-data-nci/gpcp/data
The code logs files are currently in /g/data/ia39/aus-ref-clim-data-nci/gpcp/code/update_log.txt
 Created:
      2018-01-30
 Last change:
      2022-05-31

 Usage:
 Inputs are:
   y - year to check/download/update the only one required
   t - timestep mon or day, default day is true
 
 Uses the following modules:
 import requests to download files and html via http
 import beautifulsoup4 to parse html
 import time and calendar to convert timestamp in filename
        to day number from 1-366 for each year
 import subprocess to run cksum as a shell command
 import argparse to manage inputs 

"""

import os, sys
import time, calendar
import argparse
import subprocess
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup


def parse_input():
    '''Parse input arguments '''

    parser = argparse.ArgumentParser(description='''
    Download GPCP daily and monthly data from the NOAA server
         https://www.ncei.noaa.gov/data/global-precipitation-climatology-project-gpcp-{tstep}/access/
    using requests to download file and BeautifulSoup to find links in webpage. 
    Usage: python gpcp.py -y <year> -t <tstep> ''',
             formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-y','--year', type=str, required=True,
                        help="year to process")
    parser.add_argument('-t','--tstep', default="daily", required=False,
              help="timestep either monthly or daily, daily is default")
    return vars(parser.parse_args())


def download_file(url, fname):
    '''Download file using requests '''

    r = requests.get(url)
    with open(fname, 'wb') as f:
        f.write(r.content)
    return 


def parse_dir(syr, url, data_dir):
    '''Parse main page for year and download new files.
    
    Find all the links for netcdf files in that year, if file does not
    exists locally then download it. If file exists, compare remote and 
    local last modified dates.
    '''

    r = requests.get(url)
    main_page = BeautifulSoup(r.content,'html.parser')
    for link in main_page.find_all('a',string=re.compile('^%s/' % syr)):
        subdir=link.get('href')
        r2 = requests.get("/".join([url,subdir]))
        year_page = BeautifulSoup(r2.content,'html.parser')
        for flink in year_page.find_all('a',string=re.compile(
                                             '^gpcp_.*\.nc$')):
            href=flink.get('href')
            local_name="/".join([data_dir,subdir[:4],href])
            if not os.path.exists(local_name):
                print(local_name, 'new')
                download_file("/".join([url,subdir,href]),
                              local_name)
    return


def extra_files(yr, data_dir):
    '''Check if there is more than one file for day in data directory'''

    files = os.listdir(data_dir + f"/{yr}")
    alldates = []
    tocheck = []
    # first check if two consecutive files have same date
    for f in files:
        fdate = f.split("_")[-2]
        if fdate in alldates:
            print(f"Found extra file for {fdate}")
            tocheck.append(fdate)
        alldates.append(fdate)
    if tocheck != []:
        for fdate in tocheck:
            doubles = [f for f in files if fdate in f]
            cr_dates = [f.split("_")[-1] for f in doubles]
            print(cr_dates)
            if cr_dates[1] > cr_dates[0]:
                fpath = doubles[0]
            else:
                fpath = doubles[1]
            os.rename(fpath, fpath.replace(f"/{yr}/","/redundant/"))
            print(f"Moved {fpath.split('/')[-1]} to redundant directory")
    return


def main():
    # read year as external argument and move to data directory
    inputs = parse_input()
    yr = inputs['year']
    tstep = inputs['tstep']
    # define url for GPCP http server and data_dir for local collection
    today = datetime.today().strftime('%Y-%m-%d')
    user = os.getenv("USER")
    root_dir = os.getenv("AUSREFDIR", "/g/data/ia39/aus-ref-clim-data-nci")
    run_dir = f"{root_dir}/gpcp/code"
    if tstep == "daily":
       data_dir = f"{root_dir}/gpcp/data/day/v1-3/tmp/"
    else:
       data_dir = f"{root_dir}/gpcp/data/mon/v2-3/tmp/"
    url=("https://www.ncei.noaa.gov/data/global-precipitation-" + 
          f"climatology-project-gpcp-{tstep}/access/")
    try:
        os.chdir(data_dir + f"/{yr}")
    except:
        os.mkdir(data_dir + f"/{yr}")
    # download/update the selected year
    print(f"Updated on {today} by {user}")
    print(f"Downloading files for {yr}")
    parse_dir(yr, url, data_dir)
    # check if there are more than one file for each date
    print("Checking for redundant files")
    extra_files(yr, data_dir)
    print("Download is complete")


if __name__ == "__main__":
    main()
