"""
Example 2. Time measurement of multiple functions run
"""

import time

from timench import Timench

tmnch = Timench()
repeats = 10
args_dict = {  # dict structure: {case_name: [args] of function func(*args), }
    'sleep_1s': [1.0, ],
    'sleep_2s': [2.0, ],
    'sleep_3s': [3.0, ]
}
kwargs_dict = None  # dict structure {case_name: {kwargs} of function func(**kwargs)}

for _ in args_dict:  # # Add functions to benchmark list
    tmnch.add_func(_, time.sleep)

tmnch.multiple_run(repeats, args_dict)  # Run multiple benchmarks

for _ in args_dict:
    print(tmnch.get_report(_))  # Print to terminal all reports

tmnch.write_reports('example_2_report.txt')  # Write all reports to txt-file
