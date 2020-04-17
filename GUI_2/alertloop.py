from alertsys import checkcond
import time

import json

def select_thres():
    with open('parameters.txt', 'r') as f:
        data = f.read()
    data = data.replace('\'', '\"')
    json_dict = json.loads(data)
    category1 = json_dict['category1']
    category2 = json_dict['category2']
    email = json_dict['email']

    if category1 == "":
        category1 = 'A'
    if category2 == "":
        category2 = '100D'

    print(category1)
    print(category2)
    print(email)

    """
    insert code here to choose thresholds based on category values
    """

    thres1 = 60
    thres2 = 10

    return (thres1, thres2, email)

# example of the function call which will be implemented in the update loop
# the threshold can be a boolean value indicating failure or a limit val
# outside loop
f = False

# inside loop
while True:
    print('waiting for update')
    if not f:
        (t1, t2, email) = select_thres()
        f = checkcond(f, t1, t2, email)
    else:
        break
    time.sleep(5)

# input("Press Enter to exit .")
# exit()
