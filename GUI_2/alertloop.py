from alertsys import checkcond
import time

import json


def select_thresh():
    """This is a function to set thresholds of parameters
    These would be used by the notification system to compare
    with the sensor values and send an email.
    Returns:
        {(int,int,str)} -- (threshold 1, thereshold 2,user's email)
    """

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

    thresh_engineTemp = 60
    thresh_tirePressure = 10
    thresh_tireDistanceKm = 110000
    thresh_oilTimehrs = 5000

    return (thresh_engineTemp, thresh_tirePressure, thresh_oilTimehrs, thresh_tireDistanceKm ,email)


# example of the function call which will be implemented in the update loop
# the threshold can be a boolean value indicating failure or a limit val
# outside loop
f = False

# inside loop
while True:
    print('waiting for update')
    if not f:
        (t1, t2, t3, t4, email) = select_thresh()
        f = checkcond(f, t1, t2, t3, t4, email)
    else:
        break
    time.sleep(5)

# input("Press Enter to exit .")
# exit()
