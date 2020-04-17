# MECH 550C Prject: Car Health Monitor System
- Authors: Ajay, Chinmay, Pranav, Sameer

## Description

-	Car Health Monitor is an application which is used to monitor different parameters
    of the car and notify the user about the part that has high probability of failure 
    in coming future.
-	Car Health Monitor is used to monitor the parameters Engine Oil and Tire Health with 
    the help of the sensor data. 
-	The sensor data is sent to a CSV file through Advanced Message queuing Protocol.
-	The data is read from the CSV file and is used for plotting failure curves for both
    parameters. 
-	On plotting the graph if the probability of failure I above certain value the user gets
    notified by an email
-	The email will notify what parameter of the car needs to be changed and must be serviced.
	This will help the customer to predict the failure of the part and assist the user to 
    avoid break down of the car due to sudden failure.


## File Structure

```
CarHealthMonitor
|
├── .gitignore
├── README.md
├── GUI_1
│   |── SimulatorGUI.py
│   ├── sender.py
│   ├── carsensors.ico
│   ├── decrease.png
│   ├── increase.png
├── GUI_2
│   ├── CODE_OF_CONDUCT.md
│   ├── alertloop.py
│   ├── alertsys.py
│   ├── MonitorGUI.py
│   ├── plotting_function.py
│   ├── receiver.py
│   └── graph.ico
```
## Description


## Execution


## Dependencies
- AMQP
    - rabbitmq-server == 3.8.2
    - Erlang/OTP == 22.2
- Python version 3.8.1
    - Python packages:
        - pandas == 1.0.1
        - numpy == 1.18.1
        - matplotlib == 3.2.1
        - json == 2.0.9
        - tkinter == 8.6
        - pika == 1.1.0
        - Python Standard Libraries
    - Python Standard Libraries
        - inspect — Inspect live objects
        - os — Miscellaneous operating system interfaces
        - time — Time access and conversions
        - smtplib — SMTP protocol client
        - csv — CSV File Reading and Writing
- pyInstaller is used to convert the following code into .exe file
- OS: Windows 10 64-bit

## IDE

- Visual Studio Code
