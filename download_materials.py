#!/usr/bin/env python3

import argparse
import requests

from os.path import isfile

parser = argparse.ArgumentParser(description='Download numbered materials')
parser.add_argument('--from',
                    dest='url',
                    required=True,
                    help='URL template, e.g. `foo.bar/slide{}.pdf`')
parser.add_argument('--auth',
                    dest='auth',
                    metavar=('USER', 'PASSWORD'),
                    default=None,
                    nargs=2,
                    help='authentication for URL')
parser.add_argument('--to',
                    dest='file',
                    required=True,
                    help='file template, e.g. `./slides/L{}.pdf`')
parser.add_argument('--first-id',
                    dest='id',
                    default=1,
                    type=int,
                    help='number of first material, default: 1')
parser.add_argument('-v',
                    dest='verbose',
                    action='store_true',
                    help='verbose mode')

args = parser.parse_args()

i = args.id - 1
while True:
    i = i + 1
    fname = args.file.format(i)

    if isfile(fname):
        # If material already exists, do not attempt to download it again
        if args.verbose:
            print('Skipped', fname)
        continue

    print('Downloading', fname, end=' ... ')
    r = requests.get(args.url.format(i), auth=args.auth)
    if r.status_code != 200:
        # Assume that no further material is available
        print('not yet available')
        break

    with open(fname, 'wb') as f:
        f.write(r.content)
    print('done')

