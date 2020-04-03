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
parser.add_option("-s", "--size", dest="groupSize", metavar="NUM", \
        help="The size of matches", default=2, type="int")
(options, args) = parser.parse_args()

# Open the roster file
try:
    team = open(options.rosterFile,'r')
except FileNotFoundError:
    sys.exit("COFFEE SPILLED: File %s not found" % options.rosterFile)
except PermissionError:
    sys.exit("COFFEE SPILLED: You cannot open file %s" % options.rosterFile)

# Randomize the list of people
people = [ (random.random(), person) for person in team]
# The sort() makes it so we don't get the same result every time
people.sort()

# Check to make sure the group size makes sense
if options.groupSize <= 1:
    sys.exit("COFFEE SPILLED: Group size %i is too small" % options.groupSize)
elif options.groupSize > len(people):
    sys.exit("COFFEE SPILLED: Group size %i is larger than the roster size %i" % \
            (options.groupSize, len(people)))


print("The next cycle of coffee break assignments:")

members = []
for _, person in people:
  members.append(person.rstrip())

i = 1
total = 1
for person in members:
    if ((total - i) + options.groupSize) > len(members):
        # We don't have enough for a full group
        break
    if i < options.groupSize:
        print("%s & " % person, end ="")
        i = i + 1
        total = total + 1
    else:
        print("%s" % person)
        i = 1
        total = total + 1
