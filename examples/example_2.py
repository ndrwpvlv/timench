"""
Example 2. Time measurement of multiple functions run
"""

import time

from timench import Timench

tmnch = Timench()
repeats = 10
env_args = {  # dict structure: {case_name: [args, kwargs] of function func(*args, **kwargs), }
    'sleep_1s': [[1.0, ], None],
    'sleep_2s': [[2.0, ], None],
    'sleep_3s': [[3.0, ], None]
}

for case_name in env_args:  # # Add functions to benchmark list
    tmnch.add_func(case_name, time.sleep)

tmnch.multiple_run(repeats, env_args)  # Run multiple benchmarks

for case_name in env_args:
    print(tmnch.get_report(case_name))  # Print to terminal all reports

tmnch.write_reports('example_2_report.txt')  # Write all reports to txt-file
