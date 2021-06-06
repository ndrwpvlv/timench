import time

from .templates import RESULTS


class Timench:
    def __init__(self):
        self.funcs = {}
        self.times = {}
        self.reports = {}

    def add_func(self, name: str, func):
        """
        Add function for time measurement to self.funcs dict

        :param name: func name as string
        :param func: function without ()
        :return: name variable
        """
        self.funcs[name] = func
        return name

    def add_results(self, name: str, times: list, report: str):
        """
        Add results of measurement to self.times and self.reports
        :param name: func name as string
        :param times: list with time values from output of time measurement
        :param report: report as string from output of time measurement
        :return:
        """
        self.times[name] = times
        self.reports[name] = report

    def get_report(self, name: str):
        return self.reports.get(name)

    def get_reports(self):
        return self.reports

    def write_reports(self, filename: str = 'timench_report.txt', names: list = None):
        if self.reports:
            if not names:
                names = [_ for _ in self.reports]
            with open(filename, 'w') as file:
                file.write('TIMENCH REPORT\n---\n')
                for name in names:
                    file.write('\nResults for %s\n' % name)
                    file.write(self.reports.get(name) or 'Report was not found\n')
        else:
            print('No reports to write. Run all tests again')

    def get_times_by_name(self, name: str):
        return self.times.get(name)

    def get_all_times(self):
        return self.times

    def run(self, name: str, repeats, *args, **kwargs):
        print('Running: %s' % name)
        times, report = self.run_func(self.funcs[name], repeats, *args, **kwargs)
        self.add_results(name, times, report)
        return report

    def multiple_run(self, repeats, args_dict: dict = None, kwargs_dict: dict = None):
        for name in self.funcs:
            self.run(name, repeats, *(args_dict.get(name) or [] if args_dict else []),
                     **(kwargs_dict.get(name) or {} if kwargs_dict else {}))

    @staticmethod
    def run_func(func, repeat_count: int = 1, *args, **kwargs):
        times = []
        for _ in range(repeat_count):
            time_start = time.perf_counter()
            func(*args, **kwargs)
            time_end = time.perf_counter()
            times.append(time_end - time_start)
        report = RESULTS % (func.__name__, sum(times), min(times), sum(times) / len(times), repeat_count)
        return times, report
