import re

from timench import Timench

# Setup
words_count = 1000
string = ' '.join(['text' for _ in range(words_count)])

tmnch = Timench()
repeats = 10000


def crop_string_0(text: str, count: int):
    minimize = text.split(' ')
    if len(minimize) > count:
        minimize = minimize[:count - 1]
    return ' '.join(minimize)


def crop_string_1(text: str, count: int):
    return ' '.join(text.split(' ')[:count - 1])


def crop_string_2(text: str, count: int):
    return re.search('^((\S+\s?){0,%s})' % count, text).group(1)


def first_n_words(text, n):
    assert n > 0
    match = re.search(r"(\S+\s){%s}\S+" % (n - 1), text)
    if not match:
        return text
    else:
        return text[match.span()[0]: match.span()[1]]


# Benchmark
funcs_dict = {
    crop_string_0.__name__: crop_string_0,
    crop_string_1.__name__: crop_string_1,
    crop_string_2.__name__: crop_string_2,
    first_n_words.__name__: first_n_words,
}
env_args = {  # dict structure: {case_name: [args, kwargs] of function func(*args, **kwargs), }
    crop_string_0.__name__: [[string, 200, ], None],
    crop_string_1.__name__: [[string, 200, ], None],
    crop_string_2.__name__: [[string, 200, ], None],
    first_n_words.__name__: [[string, 200, ], None],
}

for case_name in funcs_dict:  # # Add functions to benchmark list
    tmnch.add_func(case_name, funcs_dict[case_name])

tmnch.multiple_run(repeats, env_args)  # Run multiple benchmarks

for case_name in env_args:
    print(tmnch.get_report(case_name))  # Print to terminal all reports

tmnch.write_reports('example_4_report.txt')  # Write all reports to txt-file
