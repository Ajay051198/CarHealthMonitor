from alertsys import checkcond
import time

# example of the function call which will be implemented in the update loop
# the threshold can be a boolean value indicating failure or a limit val
# outside loop
f = False
# inside loop
for i in range(40):
    print('waiting for update')
    if not f:
        f = checkcond(f, 13, 13, 13)
    else:
        break
    time.sleep(5)


input("Press Enter to exit .")
exit()
