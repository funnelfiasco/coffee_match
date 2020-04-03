# coffee_match.py

Copyright 2020 by Ben Cotton.
Licensed under the [copyleft-next license](https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.1).

coffee_match is a tool to help remote teams develop social bonds by randomly
sorting a provided roster into groups to have informal meetings. A "coffee
coordinator" runs the script and sends out the matches. Then the matched people
schedule a meeting among themselves to talk about whatever.

## Usage

coffee_match reads the roster from a plain-text file, one line per participant.

coffee_match accepts the following options:

| Option | Description
| ------ | -----------
| -h, --help | show this help message and exit
|  -f FILE, --file=FILE | The roster file to use
| --remainder={skip,accept,merge} | How to deal with remainders (see below)
| -s SIZE, --size=SIZE | The size of group to create

### Remainders

Sometimes your team doesn't divide evenly by your group size.
In this case, you have three options:

* **"skip" (default)**: The remaining people don't get included in a match this time
* **"accept"**: The last group will be smaller, and that's okay. (*Note: if the final group is of size 1, we don't currently do anything about that. It's a risk you take*)
* **"merge"**: Make the last group bigger by adding all of the remaining people to it.

## Requirements

coffee_match requires Python 3 with the following modules:

* optparse
* random
* sys

## Contributing

Contributions to this project are accepted under the [copyleft-next license](https://github.com/copyleft-next/copyleft-next/blob/master/Releases/copyleft-next-0.3.1).
In other words, inbound equals outbound.

All contributors agree to abide by the [Contributor Covenant](https://www.contributor-covenant.org/).
See `code_of_conduct.md` in this repo.
