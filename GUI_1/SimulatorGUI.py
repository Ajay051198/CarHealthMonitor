from tkinter import *
import math
import os
import sys
import inspect
from tkinter import ttk

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import sender

window = Tk()

window.iconbitmap(r'carsensors.ico')

window.title("Car Health Monitor")

# width_value = (window.winfo_screenwidth() / 2)
# height_value = (window.winfo_screenheight() / 2)

# x = (window.winfo_screenwidth() // 15) - (width_value // 15)
# y = (window.winfo_screenheight() // 10) - (height_value // 10)

# window.geometry("%dx%d+%d+%d" % (width_value, height_value, x, y))

# window.minsize(math.ceil(width_value), math.ceil(height_value))
# window.maxsize(math.ceil(width_value), math.ceil(height_value))
window.minsize(800, 600)
window.maxsize(800, 600)
window.configure(bg='black')

temp = 10
press = 0
oil_time_days = 0
tire_time_months = 0
mailID = StringVar()
email = "ABC@email.com"

# setting up the font size and style
fontstyle = "Helvetica"
small_fsize = 13
large_fsize = 15
combostyle = ttk.Style()
combostyle.theme_create('combostyle', parent='alt',
                        settings={'TCombobox':
                                      {'configure':
                                           {'selectbackground': 'black',
                                            'fieldbackground': 'black',
                                            'background': 'dark grey',
                                            'arrowcolor': 'black',
                                            'bordercolor': 'white'

                                            }}})
combostyle.theme_use('combostyle')

# Initializing an object of sender
rabbit_mq = sender.RabbitMq(queue='Hello',
                            host='localhost',
                            exchange='',
                            routing_key='Hello')

x = 0
sensor1Data = []
sensor2Data = []

# Main title
lbl_Title = Label(window, text="\n Sensor Data \n", bg="black", fg="white", font=(large_fsize, large_fsize))

lbl_Temp = Label(window, text="Engine Temperature (°C)", font=(fontstyle, small_fsize), bg="black", fg="white")
# lbl_blank1 = Label(window, text=" ", bg="black")
lbl_Press = Label(window, text="Tire Pressure (psi)", font=(fontstyle, small_fsize), bg="black", fg="white")
lbl_blank2 = Label(window, text="  ", bg="black")

lbl_cat1 = Label(window, text="Car Make", font=(fontstyle, small_fsize), bg="black", fg="white")
lbl_blank3 = Label(window, text="  ", bg="black")
lbl_cat2 = Label(window, text="Ambient Driving Condition", font=(fontstyle, small_fsize), bg="black", fg="white")
lbl_blank4 = Label(window, text="  ", bg="black")

lbl_heading = Label(window, text="\nTime elapsed after last replacement\n ", bg="black", fg="white",
                    font=(fontstyle, large_fsize))
lbl_blank5 = Label(window, text="   ", bg="black")

lbl_oilTime = Label(window, text="For Oil (in days)", font=(fontstyle, small_fsize), bg="black", fg="white")
lbl_blank3 = Label(window, text="           ", bg="black")
lbl_tireTime = Label(window, text="For Tire (in months)", font=(fontstyle, small_fsize), bg="black", fg="white")
lbl_blank6 = Label(window, text="  \n ", bg="black")
lbl_blank7 = Label(window, text="  \n ", bg="black")

email_input = Entry(window, textvariable=mailID, bg="dark grey", font=(fontstyle, large_fsize), fg="black")
lbl_blank8 = Label(window, text="        \n   ", bg="black")
lbl_email = Label(window, text="Please enter email id to receive notifications", font=(fontstyle, small_fsize),
                  bg="black", fg="white")

count_Temp = Label(window, text=temp, bg="black", fg="white", font=(fontstyle, small_fsize))
count_Press = Label(window, text=press, bg="black", fg="white", font=(fontstyle, small_fsize))
count_oil_time = Label(window, text=oil_time_days, bg="black", fg="white", font=(fontstyle, small_fsize))
count_tire_time = Label(window, text=tire_time_months, bg="black", fg="white", font=(fontstyle, small_fsize))

makes = ['A', 'B', 'C', 'D']
make_select = ttk.Combobox(window, values=makes, width=0)
models = ['100D', '200D', '300D', '400D']
model_select = ttk.Combobox(window, values=models, width=0)

# grid layout
lbl_Title.grid(row=0, column=1, sticky=N + S + E + W, columnspan=3)

lbl_Temp.grid(row=4, column=0, sticky=N + S + E + W)
# lbl_blank1.grid(row=5, column=0, sticky=N + S + E + W)

lbl_Press.grid(row=6, column=0, sticky=N + S + E + W)
lbl_blank2.grid(row=7, column=0, sticky=N + S + E + W)

lbl_cat1.grid(row=8, column=0, sticky=N + S + E + W)
lbl_blank3.grid(row=9, column=0, sticky=N + S + E + W)

lbl_cat2.grid(row=10, column=0, sticky=N + S + E + W)
lbl_blank4.grid(row=11, column=0, sticky=N + S + E + W)

lbl_heading.grid(row=12, column=1, sticky=N + S + E + W, columnspan=3)
lbl_blank5.grid(row=13, column=0, sticky=N + S + E + W)

lbl_oilTime.grid(row=14, column=0, sticky=N + S + E + W)
lbl_blank6.grid(row=15, column=4, sticky=N + S + E + W)

lbl_tireTime.grid(row=16, column=0, sticky=N + S + E + W)
lbl_blank7.grid(row=17, column=4, sticky=N + S + E + W)

email_input.grid(row=18, column=2, sticky=N + S + E + W)
lbl_email.grid(row=18, column=0, sticky=N + S + E + W, columnspan=1)
lbl_blank8.grid(row=19, column=4, sticky=N + S + E + W)

count_Temp.grid(row=4, column=2, sticky=N + S + E + W)
count_Press.grid(row=6, column=2, sticky=N + S + E + W)
make_select.grid(row=8, column=2, sticky=N + S + E + W)
model_select.grid(row=10, column=2, sticky=N + S + E + W)
count_oil_time.grid(row=14, column=2, sticky=N + S + E + W)
count_tire_time.grid(row=16, column=2, sticky=N + S + E + W)

img_increase = PhotoImage(file='increase.png')
img_decrease = PhotoImage(file='decrease.png')


def increase_temp():
    global temp
    temp = temp + 10
    count_Temp.configure(text=temp)


def decrease_temp():
    global temp
    if temp > 0:
        temp = temp - 10
        count_Temp.configure(text=temp)


def increase_press():
    global press
    if press < 40:
        press = press + 1
        count_Press.configure(text=press)


def decrease_press():
    global press
    if press > 0:
        press = press - 1
        count_Press.configure(text=press)


def increase_oilTime():
    global oil_time_days
    oil_time_days = oil_time_days + 1
    count_oil_time.configure(text=oil_time_days)


def decrease_oilTime():
    global oil_time_days
    if oil_time_days > 0:
        oil_time_days = oil_time_days - 1
        count_oil_time.configure(text=oil_time_days)


def increase_tireTime():
    global tire_time_months
    tire_time_months = tire_time_months + 3
    count_tire_time.configure(text=tire_time_months)


def decrease_tireTime():
    global tire_time_months
    if tire_time_months > 0:
        tire_time_months = tire_time_months - 3
        count_tire_time.configure(text=tire_time_months)


def transmit():
    global mailID
    global email
    email = mailID.get()


btn_decTemp = Button(window, image=img_decrease, command=decrease_temp,
                     bg="black", borderwidth=0, activebackground="black")
btn_incTemp = Button(window, image=img_increase, command=increase_temp,
                     bg="black", borderwidth=0, activebackground="black")
btn_incPress = Button(window, image=img_decrease, command=decrease_press,
                      bg="black", borderwidth=0, activebackground="black")
btn_decPress = Button(window, image=img_increase, command=increase_press,
                      bg="black", borderwidth=0, activebackground="black")
btn_decOilTime = Button(window, image=img_decrease, command=decrease_oilTime, bg="black", borderwidth=0,
                        activebackground="black")
btn_incOilTime = Button(window, image=img_increase, command=increase_oilTime, bg="black", borderwidth=0,
                        activebackground="black")
btn_decTireTime = Button(window, image=img_decrease, command=decrease_tireTime, bg="black", borderwidth=0,
                         activebackground="black")
btn_incTireTime = Button(window, image=img_increase, command=increase_tireTime, bg="black", borderwidth=0,
                         activebackground="black")
btn_mailID = Button(window, text="Enter", command=transmit, bg="black", fg="white", height=2, width=4)

btn_decTemp.grid(row=4, column=1, sticky=N + S + E + W)
btn_incTemp.grid(row=4, column=3, sticky=N + S + E + W)
btn_incPress.grid(row=6, column=1, sticky=N + S + E + W)
btn_decPress.grid(row=6, column=3, sticky=N + S + E + W)
btn_decOilTime.grid(row=14, column=1, sticky=N + S + E + W)
btn_incOilTime.grid(row=14, column=3, sticky=N + S + E + W)
btn_decTireTime.grid(row=16, column=1, sticky=N + S + E + W)
btn_incTireTime.grid(row=16, column=3, sticky=N + S + E + W)
btn_mailID.grid(row=18, column=3, sticky=N + S + E + W)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

window.grid_rowconfigure(0, weight=4)
window.grid_rowconfigure(5, weight=4)


def timer():
    global x

    if x < 10000:
        window.after(1000, timer)  # call this function again in 1,000 milliseconds
        print("Updating ...")
        # time_text = "Timer: {} weeks".format(x)
        # timer_display.configure(text=time_text)

        # rabbit_mq.publish(payload=temp)
        sensor1Data.append(temp)
        sensor2Data.append(press)

        category1 = model_select.get()
        category2 = make_select.get()
        # store 10 reading in a list and then publish at once
        if len(sensor1Data) == 10:
            rabbit_mq.publish(payload={"sensor1Data": sensor1Data,
                                       "sensor2Data": sensor2Data,
                                       "oilTime_hrs": oil_time_days * 24,
                                       "tireTime_years": tire_time_months / 12,
                                       "email": email,
                                       "category1": category1,
                                       "category2": category2})
            sensor2Data.clear()
            sensor1Data.clear()
            # print(f"Value f x is{x}")
            # to set an infinite loop to continuously send data
            if x > 100:
                x = 0
        x += 1


timer()
window.mainloop()
