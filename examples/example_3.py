"""
Example 3. Time measurement with context execution
"""

import time

from timench import Timench

with Timench():  # Run time measurement for some code
    time.sleep(1.0)
    time.sleep(2.0)
    time.sleep(3.0)
