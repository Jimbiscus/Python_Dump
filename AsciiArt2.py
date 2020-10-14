import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.07)

delay_print(":-=-=-=-=-=-=-=-=-: \n")
delay_print("Stats of Jimbus \n")
delay_print(":-=-=-=-=-=-=-=-:")
