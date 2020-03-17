# coffee_match.py

Copyright 2020 by Ben Cotton.
Licensed under the [copyleft-next license](https://github.com/copyleft-next/copyleft-next/blob/v0.3.0/Releases/copyleft-next-0.3.0).

coffee_match is a tool to help remote teams develop social bonds by randomly
sorting a provided roster into groups to have informal meetings. A "coffee
coordinator" runs the script and sends out the matches. Then the matched people
schedule a meeting among themselves to talk about whatever.

## Usage

coffee_match reads the roster from a plain-text file, one line per participant.

coffee_match accepts the following options:

| Option | Description
| ====== | ===========
|   -h, --help | show this help message and exit
  -f FILE, --file=FILE | The roster file to use

## Requirements

coffee_match requires Python 3 with the following modules:

* optparse
* random
* sys
