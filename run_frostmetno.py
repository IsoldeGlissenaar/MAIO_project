#!/usr/bin/python

"""

This program shows how to retrieve a time series of observations from the following
combination of source, element and time range:

source:     SN99840
element:    mean(wind_speed P1D)
time range: 2010-04-01 .. 2010-05-31

The time series is written to standard output as lines of the form:

  <observation time as date/time in ISO 8601 format> \
  <observation time as seconds since 1970-01-01T00:00:00> \
  <observed value>

Save the program to a file example.py, make it executable (chmod 755 example.py),
and run it e.g. like this:

  $ CLIENTID=2733ff4d-c1a0-4bba-877e-d68dba5b99ef ./example.py

(Note: the client ID used in the example should be replaced with a real one)

The program has been tested on the following platforms:
  - Python 2.7.3 on Ubuntu 12.04 Precise
  - Python 2.7.12 and 3.5.2 on Ubuntu 16.04 Xenial

"""

import sys, os
import dateutil.parser as dp
import requests # See http://docs.python-requests.org/

if __name__ == "__main__":

    # extract client ID from environment variable
    if not 'CLIENTID' in os.environ:
        sys.stderr.write('error: CLIENTID not found in environment\n')
        sys.exit(1)
    client_id = os.environ['CLIENTID']

    # issue an HTTP GET request
    r = requests.get(
        'https://frost.met.no/observations/v0.jsonld',
        {'sources': 'SN99840', 'elements': 'mean(wind_speed P1D)', 'referencetime': '2010-04-01/2010-06-01'},
        auth=(client_id, '')
    )

    # extract the time series from the response
    if r.status_code == 200:
        for item in r.json()['data']:
            iso8601 = item['referenceTime']
            secsSince1970 = dp.parse(iso8601).strftime('%s')
            sys.stdout.write('{} {} {}\n'.format(iso8601, secsSince1970, item['observations'][0]['value']))
    else:
        sys.stdout.write('error:\n')
        sys.stdout.write('\tstatus code: {}\n'.format(r.status_code))
        if 'error' in r.json():
            assert(r.json()['error']['code'] == r.status_code)
            sys.stdout.write('\tmessage: {}\n'.format(r.json()['error']['message']))
            sys.stdout.write('\treason: {}\n'.format(r.json()['error']['reason']))
        else:
            sys.stdout.write('\tother error\n')
    