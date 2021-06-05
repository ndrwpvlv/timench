import time

from .templates import RESULTS


class Timench:
    def __init__(self):
        self.funcs = {}
        self.times = {}
        self.reports = {}

    def add_func(self, name: str, func):
        self.funcs[name] = func
        return name

    def add_results(self, name: str, times: list, report: str):
        self.times[name] = times
        self.reports[name] = report

    def run(self, name: str, repeats, *args, **kwargs):
        print('Running: %s' % name)
        times, report = self.run_func(self.funcs[name], repeats, *args, **kwargs)
        self.add_results(name, times, report)
        return report

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
                    file.write('Results for %s\n' % name)
                    file.write(self.reports.get(name) or 'Report was not found\n')
        else:
            print('No reports to write. Run all tests again')

    def get_times_by_name(self, name: str):
        return self.times.get(name)

    def get_all_times(self):
        return self.times

    @staticmethod
    def run_func(func, repeat_count: int = None, *args, **kwargs):
        times = []
        for _ in range(repeat_count or 1):
            time_start = time.time()
            func(*args, **kwargs)
            time_end = time.time()
            times.append(time_end - time_start)
        report = RESULTS % (sum(times), min(times), sum(times) / len(times), repeat_count)
        return times, report
