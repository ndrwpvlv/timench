import random
from timench import Timench

# Setup

lst_1 = [[i, i + 1] for i in range(100)]
lst_2 = [[i, i + 1] for i in range(1000)]
lst_3 = [[i, i + 1] for i in range(10000)]


tmnch = Timench()
repeats = 100


def flat(lst: list):
    return [item for row in lst for item in row]


def sum_lst(lst: list):
    return sum(lst, [])


# Benchmark
funcs_dict = {
    'sum_1': sum_lst,
    'flat_1': flat,
    'sum_2': sum_lst,
    'flat_2': flat,
    'sum_3': sum_lst,
    'flat_3': flat,
}
env_args = {  # dict structure: {case_name: [args, kwargs] of function func(*args, **kwargs), }
    'sum_1': [[lst_1, ], None],
    'flat_1': [[lst_1, ], None],
    'sum_2': [[lst_2, ], None],
    'flat_2': [[lst_2, ], None],
    'sum_3': [[lst_3, ], None],
    'flat_3': [[lst_3, ], None],
}

for case_name in funcs_dict:  # # Add functions to benchmark list
    tmnch.add_func(case_name, funcs_dict[case_name])

tmnch.multiple_run(repeats, env_args)  # Run multiple benchmarks

for case_name in env_args:
    print(tmnch.get_report(case_name))  # Print to terminal all reports

tmnch.write_reports('example_5_report.txt')  # Write all reports to txt-file
