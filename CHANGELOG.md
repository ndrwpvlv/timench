
# Change Log

## [0.2.0]

## Changed

Changed `Timench.multiple_run()` method and structure of it input of variable `*args` and `**kwargs` for multiple benchmarks run. 

Before it was two separated dicts for args `{case_name: [args, ]}`, for kwargs `{case_name: {kwargs, }}`.
Now it is combined to single dict to simplify input of variables and control of it.

New structure named as `env_args = {case_name: [[args], {kwargs, }], }`

## Updated

Usage examples 2 and 4 updated for correct run with updated `multiple_run()` method.

## [0.1.0]
  
Initial release
