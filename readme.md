# IP Query System

A simple IP query system that looks through a log of IP addresses that have visited a website and loads them
into a quick querying system.

# Assumptions

I am assuming that lookups will be done with the current logs and that they are done with a concatenated
log file. This is done simply for the sake of complexity.

I am assuming lookups are done in constant - O(1) - time as described in the
[Python Wiki Time Complexity document](https://wiki.python.org/moin/TimeComplexity). This could vary based on
operating system and environment, however, due to the way hashcodes are generated for strings differs on various
systems.

Finally, I am assuming that multiple lookups will be done while the system is running. If only one lookup is done per
run, then a different solution with O(1) space complexity can be used. With multiple lookups a map is set up that
allows for quick lookups with O(1) time complexity after the initial load time done in O(n).

# Limitations

The only real limitations of this system is the size of the log file. If this is run on a 32-bit system, then the
log file can only be run on a 4 GB log. For a production system that can handle half a billion hits, this would need
to be changed to read multiple log files since only 100,000 IP addresses can be held in a 1.5 MB file.

# Dependencies

The only required dependency is a system that can run Python.