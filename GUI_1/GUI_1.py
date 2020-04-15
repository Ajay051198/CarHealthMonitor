from tkinter import *
import math
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import sender

window = Tk()

window.iconbitmap(r'carsensors.ico')

window.title("Car Health Monitor")

width_value = (window.winfo_screenwidth() / 2.5)
height_value = (window.winfo_screenheight() / 2.5)

x = (window.winfo_screenwidth() // 15) - (width_value // 15)
y = (window.winfo_screenheight() // 10) - (height_value // 10)

window.geometry("%dx%d+%d+%d" % (width_value, height_value, x, y))

window.minsize(math.ceil(width_value), math.ceil(height_value))
window.maxsize(math.ceil(width_value), math.ceil(height_value))

window.configure(bg='black')

fontstyle = "Helvetica"
small_fsize = 13
large_fsize = 15

temp = 100
press = 32
oil_time = 0
tire_time = 0

# Initializing an object of sender
rabbit_mq = sender.RabbitMq(queue='Hello',
                            host='localhost',
                            exchange='',
                            routing_key='Hello')

x = 0
sensor1Data = []
sensor2Data = []


def timer():
    global x

    if x < 150:
        # message.set(temp)
        window.after(1000, timer)  # call this function again in 1,000 milliseconds
        # sender.RabbitMq(str(Sensor1Val))
        print("im here")

        try:
            # rabbit_mq.publish(payload=temp)
            sensor1Data.append(temp)
            sensor2Data.append(press)

            # store 10 reading in a list and then publish at once
            if len(sensor1Data) == 10:
                #we convert oil_time from days to hours
                rabbit_mq.publish(payload=[sensor1Data, sensor2Data, oil_time*24, tire_time])
                sensor2Data.clear()

                sensor1Data.clear()
                # print(f"Value f x is{x}")
                # to set an infinite loop to continuously send data
                if x > 100:
                    x = 0

        except:
            print("Fucked")
        x += 1


# message = IntVar()
# message.set(temp)

# timer_display = Label(window, textvar=message, font=("Arial Bold", 15))
# timer_display.place(x=100, y=80, anchor=CENTER)

lbl1 = Label(window, text="\n Input Sensor Data \n \n", bg="black", fg="white", font=(fontstyle, large_fsize))

lbl_Temp = Label(window, text="Engine Temperature(°C) ", font=(fontstyle, small_fsize), bg="black", fg="white")
lbl_blank1 = Label(window, text="  ", bg="black")
lbl_Press = Label(window, text="Tire Pressure (psi)", font=(fontstyle, small_fsize), bg="black", fg="white")
lbl_blank2 = Label(window, text="  ", bg="black")

lbl_heading = Label(window, text="\nTime elapsed after last replacement\n \n", bg="black", fg="white", font=(fontstyle, large_fsize))

lbl_oilTime = Label(window, text="For Oil (in days)", font=(fontstyle, small_fsize), bg="black", fg="white")
lbl_blank3 = Label(window, text="           ", bg="black")
lbl_tireTime = Label(window, text="For Tire (in months)", font=(fontstyle, small_fsize), bg="black", fg="white")
lbl_blank4 = Label(window, text="  \n ", bg="black")
lbl_blank5 = Label(window, text="  \n ", bg="black")
# lbl_blank2 = Label(window, text="  ", bg="black")

count_Temp = Label(window, text=temp, bg="black", fg="white", font=(fontstyle, small_fsize))
count_Press = Label(window, text=press, bg="black", fg="white", font=(fontstyle, small_fsize))
count_oil_time = Label(window, text=oil_time, bg="black", fg="white", font=(fontstyle, small_fsize))
count_tire_time = Label(window, text=tire_time, bg="black", fg="white", font=(fontstyle, small_fsize))

lbl1.grid(row=0, column=1, sticky=N + S + E + W, columnspan =3)
lbl_Temp.grid(row=2, column=0, sticky=N + S + E + W)
lbl_blank1.grid(row=4, column=0, sticky=N + S + E + W)
lbl_Press.grid(row=5, column=0, sticky=N + S + E + W)
lbl_blank2.grid(row=7, column=0, sticky=N + S + E + W)
lbl_heading.grid(row=8, column=1, sticky=N + S + E + W,columnspan=3)
lbl_oilTime.grid(row=9, column=0, sticky=N + S + E + W)
lbl_blank3.grid(row=10, column=4, sticky=N + S + E + W)
lbl_tireTime.grid(row=11, column=0, sticky=N + S + E + W)
lbl_blank4.grid(row=12, column=0, sticky=N + S + E + W)
lbl_blank5.grid(row=13, column=0, sticky=N + S + E + W)

count_Temp.grid(row=2, column=2, sticky=N + S + E + W)
count_Press.grid(row=5, column=2, sticky=N + S + E + W)
count_oil_time.grid(row=9, column=2, sticky=N + S + E + W)
count_tire_time.grid(row=11, column=2, sticky=N + S + E + W)

img_increase = PhotoImage(file='increase.png')
img_decrease = PhotoImage(file='decrease.png')


def increasetemp():
    global temp
    temp = temp + 10
    count_Temp.configure(text=temp)


def decreasetemp():
    global temp
    if temp > 0:
        temp = temp - 10
        count_Temp.configure(text=temp)


def increasepress():
    global press
    if press < 40:
        press = press + 1
        count_Press.configure(text=press)


def decreasepress():
    global press
    if press > 0:
        press = press - 1
        count_Press.configure(text=press)


def increase_oilTime():
    global oil_time
    oil_time = oil_time + 1
    count_oil_time.configure(text=oil_time)


def decrease_oilTime():
    global oil_time
    if oil_time > 0:
        oil_time = oil_time - 1
        count_oil_time.configure(text=oil_time)


def increase_tireTime():
    global tire_time
    tire_time = tire_time + 3
    count_tire_time.configure(text=tire_time)


def decrease_tireTime():
    global tire_time
    if tire_time > 0:
        tire_time = tire_time - 3
        count_tire_time.configure(text=tire_time)


btn_decTemp = Button(window, image=img_decrease, command=decreasetemp, bg="black", borderwidth=0,
                     activebackground="black")
btn_incTemp = Button(window, image=img_increase, command=increasetemp, bg="black", borderwidth=0,
                     activebackground="black")
btn_incPress = Button(window, image=img_decrease, command=decreasepress, bg="black", borderwidth=0,
                      activebackground="black")
btn_decPress = Button(window, image=img_increase, command=increasepress, bg="black", borderwidth=0,
                      activebackground="black")
btn_decOilTime = Button(window, image=img_decrease, command=decrease_oilTime, bg="black", borderwidth=0,
                        activebackground="black")
btn_incOilTime = Button(window, image=img_increase, command=increase_oilTime, bg="black", borderwidth=0,
                        activebackground="black")
btn_decTireTime = Button(window, image=img_decrease, command=decrease_tireTime, bg="black", borderwidth=0,
                         activebackground="black")
btn_incTireTime = Button(window, image=img_increase, command=increase_tireTime, bg="black", borderwidth=0,
                         activebackground="black")

btn_decTemp.grid(row=2, column=1, sticky=N + S + E + W)
btn_incTemp.grid(row=2, column=3, sticky=N + S + E + W)
btn_incPress.grid(row=5, column=1, sticky=N + S + E + W)
btn_decPress.grid(row=5, column=3, sticky=N + S + E + W)
btn_decOilTime.grid(row=9, column=1, sticky=N + S + E + W)
btn_incOilTime.grid(row=9, column=3, sticky=N + S + E + W)
btn_decTireTime.grid(row=11, column=1, sticky=N + S + E + W)
btn_incTireTime.grid(row=11, column=3, sticky=N + S + E + W)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

window.grid_rowconfigure(0, weight=4)
window.grid_rowconfigure(5, weight=4)

timer()
window.mainloop()
