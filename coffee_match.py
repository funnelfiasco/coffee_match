#!/usr/bin/env python3

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
