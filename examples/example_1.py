"""
Example 1. Time measurement of function single run
"""

import time

from timench import Timench

tmnch = Timench()
case_name = 'sleep_1sec'  # Set run case name
repeats = 10  # Count of repeats
sleep_time = 1.0  # args of time.sleep(sleep_time)

tmnch.add_func(case_name, time.sleep)  # Add function to benchmark list

tmnch.run(case_name, repeats, sleep_time)  # Run benchmark
print(tmnch.get_report(case_name))  # Print benchmark report

tmnch.write_reports('example_1_report.txt')  # Write all reports to txt-file
