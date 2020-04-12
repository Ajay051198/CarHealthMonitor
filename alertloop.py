from alertsys import checkcond
import time

# example of the fucntion call which will be implemented in the update loop
# the threshold can be a bollean value indicating faliure or a limit val
# outside loop
f = False
# inside loop
for i in range(40):
    print('waiting for update')
    if f == False:
        f = checkcond(f, 13,13,13)
    else:
        break
    time.sleep(5)


input("Press Enter to exit .")
exit()
