import pandas as pd
import smtplib

debug = False

def send_email(from_addr, to_addr_list, cc_addr_list,
               subject, message,
               login, password,
               smtpserver='smtp.gmail.com:587'):
    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

def checkcond(f, thres1 = 10, thres2 = 10, thres3 = 10):
    data = pd.read_csv('SensorData.csv')
    data.columns = ['DataStream1', 'DataStream2', 'DataStream3']
    data = data.tail(10)

    # using flag based calling to ensure the alert is given only once unless it is reset
    flag = f
    message = ""

    # temperory print line meant for debuging
    print(data['DataStream1'].mean(), data['DataStream2'].mean(), data['DataStream3'].mean())

    # checking the mean of the last 10 values to avoid triggers by noise
    if data['DataStream1'].mean() > thres1:
        message = message + "component 1 requires maintainance \n"
        flag = True

    if data['DataStream2'].mean() > thres2:
        message = message + "component 2 requires maintainance \n"
        flag = True

    if data['DataStream3'].mean() > thres3:
        message = message + "component 3 requires maintainance \n"
        flag = True

    if flag == True:

        print(message)
        # the below section will be in the final code
        '''
        send_email(from_addr='s1lv3r.b0t@gmail.com',
                   to_addr_list=['ajay.selvamk@gmail.com'],
                   subject='Howdy',
                   message='Howdy from a python function',
                   login='s1lv3r.b0t@gmail.com',
                   password='1111111111111111') # will not work as i cant put my password here
        '''
    return flag

if debug == True:
    # example of the fucntion call which will be implemented in the update loop
    # the threshold can be a bollean value indicating faliure or a limit val
    # outside loop
    f = False
    # inside loop
    for i in range(10):
        if f == False:
            f = checkcond(f, 15,15,15)

    input("Press Enter to exit .")
    exit()
