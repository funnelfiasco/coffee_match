#!/usr/bin/env python3

#####
#
# coffee_match.py - a tool for matching teams at random for coffee breaks
#
# Copyright 2020 by Ben Cotton
# Distributed under the copyleft-next license:
#     https://github.com/copyleft-next/copyleft-next/blob/v0.3.0/Releases/copyleft-next-0.3.0
#
#####

from optparse import OptionParser
import random
import sys

# Set up the parser
parser = OptionParser()
parser.add_option("-f", "--file", dest="rosterFile", metavar="FILE", \
    help="The roster file to use", default="team.txt")
(options, args) = parser.parse_args()

# Open the roster file
try:
    team = open(options.rosterFile,'r')
except FileNotFoundError:
    sys.exit("COFFEE SPILLED: File %s not found" % options.rosterFile)
except PermissionError:
    sys.exit("COFFEE SPILLED: You cannot open file %s" % options.rosterFile)

i=0

# Randomize the list of people
people = [ (random.random(), person) for person in team]
# The sort() makes it so we don't get the same result every time
people.sort()

print("The next cycle of coffee break assignments:")

members = []
for _, person in people:
  members.append(person.rstrip())

for person1, person2 in zip(members[0::2], members[1::2]):
  # Only print if there are two people
  print("* %s & %s" % (person1, person2))
