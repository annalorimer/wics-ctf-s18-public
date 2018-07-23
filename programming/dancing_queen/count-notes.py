#!/usr/bin/env python3

with open("Goin' Under.sm") as f:
    relevant_lines = [ line for line in f if len(line) == 5 ]
    first = 0
    second = 0
    third = 0
    fourth = 0
    for line in relevant_lines:
        if line[0] != '0': first += 1
        if line[1] != '0':
            print(line)
            second += 1
        if line[2] != '0': third += 1
        if line[3] != '0': fourth += 1
    print(first, second, third, fourth)
