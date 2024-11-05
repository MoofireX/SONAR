import RPi.GPIO  as gpio
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from matplotlib import style

style.use('fivethirtyeight')


trigger = 7
echo = 11

x_list = []
y_list = []


figure = plt.figure()
axis = figure.add_subplot(1,1,1)

gpio.setmode(gpio.BOARD)

gpio.setup(trigger, gpio.OUT)
gpio.setup(echo, gpio.IN)

counter = 1

while True:
    gpio.output(trigger, gpio.LOW)
    print("sleeping")
    time.sleep(2)

    print("Ranging")
    gpio.output(trigger, gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(trigger, gpio.LOW)

    while gpio.input(echo) == 0:
        pulse_start = time.time()
    while gpio.input(echo) == 1:
        pulse_end = time.time()

        pulse_time = pulse_end - pulse_start

    distance = pulse_time * 17150


    y_list.append(int(distance-(distance*2)))
    x_list.append(counter)

    plt.plot(x_list,y_list)
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1))

    if counter != 1:
        plt.show()
    
    counter += 1

gpio.cleanup()
