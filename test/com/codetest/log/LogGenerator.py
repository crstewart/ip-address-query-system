#!/usr/bin/env python

"""
Code based on log generation snippet provided in the exercise.
"""
import sys
import random

LOGFILE_LOCATION = "../../../../logs/visitors.log"


class LogGenerator:
    def main(self, count):
        logfile = open(LOGFILE_LOCATION, "w")
        for x in xrange(count):
            first_number = random.randint(0, 255)
            second_number = random.randint(0, 255)
            third_number = random.randint(0, 255)
            fourth_number = random.randint(0, 255)
            logfile.write("%d.%d.%d.%d\n" % (first_number, second_number, third_number, fourth_number))

if __name__ == "__main__":
    count = 10
    if len(sys.argv) > 1:
        count = int(sys.argv[1])

    mainObj = LogGenerator()
    mainObj.main(count)
