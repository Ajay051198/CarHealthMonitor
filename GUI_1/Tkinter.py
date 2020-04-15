from tkinter import *
import math
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
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

window.configure(bg='black')

temp = 10
press = 0
emissions = 0
timeElapsed=20


#Initializing an object of sender
rabbit_mq = sender.RabbitMq(queue='Hello',
                            host='localhost',
                            exchange='',
                            routing_key='Hello')

x = 0
sensor1Data=[]
sensor2Data=[]
sensor3Data=[]
def timer():
    global x

    if x < 150:
        message.set(temp)
        window.after(1000, timer) # call this function again in 1,000 milliseconds
        # sender.RabbitMq(str(Sensor1Val))
        print("im here")
        
        try:
            # rabbit_mq.publish(payload=temp)
            sensor1Data.append(temp)
            sensor2Data.append(press)
            sensor3Data.append(emissions)
            #store 10 reading in a list and then publish at once
            if len(sensor1Data)==10:
                rabbit_mq.publish(payload=[sensor1Data,sensor2Data,sensor3Data,timeElapsed])
                sensor2Data.clear()
                sensor3Data.clear()
                sensor1Data.clear()
                # print(f"Value f x is{x}")
                # to set an infinite loop to continuesly send data
                if x>100:
                    x=0 

        except:
            print("Fucked")
        x += 1

message = IntVar()
message.set(temp)

timer_display = Label(window, textvar= message,font=("Arial Bold", 15))
timer_display.place(x= 100, y= 80, anchor = CENTER)

lbl1 = Label(window, text="\n Input Sensor Data \n \n", bg="black", fg="white", font=("Times New Roman", 20))

lbl_Temp = Label(window, text="Car Temperature", font=("Times New Roman", 15), bg="black", fg="white")
lbl_blank1 = Label(window, text="  ", bg="black")
lbl_Press = Label(window, text="Tire Pressure", font=("Times New Roman", 15), bg="black", fg="white")
lbl_blank2 = Label(window, text="  ", bg="black")
lbl_emissions = Label(window, text="Emissions", font=("Times New Roman", 15), bg="black", fg="white")
lbl_blank3 = Label(window, text="           ", bg="black")
lbl_blank4 = Label(window, text="  \n ", bg="black")
# lbl_blank2 = Label(window, text="  ", bg="black")

count_Temp = Label(window, text=temp, bg="black", fg="white", font=("Times New Roman", 26))
count_Press = Label(window, text=press, bg="black", fg="white", font=("Times New Roman", 26))
count_emissions = Label(window, text=emissions, bg="black", fg="white", font=("Times New Roman", 26))

lbl1.grid(row=0, column=2, sticky=N + S + E + W)
lbl_Temp.grid(row=2, column=0, sticky=N + S + E + W)
lbl_blank1.grid(row=4, column=0, sticky=N + S + E + W)
lbl_Press.grid(row=5, column=0, sticky=N + S + E + W)
lbl_blank2.grid(row=7, column=0, sticky=N + S + E + W)
lbl_emissions.grid(row=8, column=0, sticky=N + S + E + W)
lbl_blank3.grid(row=8, column=4, sticky=N + S + E + W)
lbl_blank4.grid(row=10, column=0, sticky=N + S + E + W)

count_Temp.grid(row=2, column=2, sticky=N + S + E + W)
count_Press.grid(row=5, column=2, sticky=N + S + E + W)
count_emissions.grid(row=8, column=2, sticky=N + S + E + W)

img_increase = PhotoImage(file='increase.png')
img_decrease = PhotoImage(file='decrease.png')


def increasetemp():
    global temp
    temp = temp + 1
    count_Temp.configure(text=temp)


def decreasetemp():
    global temp
    temp = temp - 1
    count_Temp.configure(text=temp)


def increasepress():
    global press
    press = press + 1
    count_Press.configure(text=press)


def decreasepress():
    global press
    press = press - 1
    count_Press.configure(text=press)


def increase_emm():
    global emissions
    emissions = emissions + 1
    count_emissions.configure(text=emissions)


def decrease_emm():
    global emissions
    emissions = emissions - 1
    count_emissions.configure(text=emissions)


btn_decTemp = Button(window, image=img_decrease, command=decreasetemp, bg="black", borderwidth=0, activebackground="black")
btn_incTemp = Button(window, image=img_increase, command=increasetemp, bg="black", borderwidth=0, activebackground="black")
btn_incPress = Button(window, image=img_decrease, command=decreasepress, bg="black", borderwidth=0, activebackground="black")
btn_decPress = Button(window, image=img_increase, command=increasepress, bg="black", borderwidth=0, activebackground="black")
btn_decEmm = Button(window, image=img_decrease, command=decrease_emm, bg="black", borderwidth=0, activebackground="black")
btn_incEmm = Button(window, image=img_increase, command=increase_emm, bg="black", borderwidth=0, activebackground="black")

btn_decTemp.grid(row=2, column=1, sticky=N + S + E + W)
btn_incTemp.grid(row=2, column=3, sticky=N + S + E + W)
btn_incPress.grid(row=5, column=1, sticky=N + S + E + W)
btn_decPress.grid(row=5, column=3, sticky=N + S + E + W)
btn_decEmm.grid(row=8, column=1, sticky=N + S + E + W)
btn_incEmm.grid(row=8, column=3, sticky=N + S + E + W)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)

window.grid_rowconfigure(0, weight=4)
window.grid_rowconfigure(5, weight=4)

timer() 
window.mainloop()
