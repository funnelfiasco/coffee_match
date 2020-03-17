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

import random

team = open('team.txt','r')
i=0

people = [ (random.random(), person) for person in team]

people.sort()

print("The next cycle of coffee break assignments:")

members = []
for _, person in people:
  members.append(person.rstrip())

for person1, person2 in zip(members[0::2], members[1::2]):
  # Only print if there are two people
  print("* %s & %s" % (person1, person2))
