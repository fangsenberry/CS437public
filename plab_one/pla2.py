from sense_hat import SenseHat
import time
import matplotlib.pyplot as plt

TIME_TO_RUN = 10

start_time = time.time()
count = 0

sense = SenseHat()

total_temp = 0

# Initialize lists to store temps
raw_temps = []
ave_temps = []

print("here")

while (time.time()-start_time) < TIME_TO_RUN:
    if (time.time()-start_time) % 1 == 0: print("time elapsed: ", time.time()-start_time)
    raw_temp = sense.get_temperature()

    # store this raw temp
    raw_temps.append(raw_temp)
    
    count += 1
    total_temp += raw_temp
    if count % 500 == 0: # calculate average every 500 readings
        ave_temp = total_temp / 500

        # store this average temperature
        ave_temps.extend([ave_temp]*500) # repeat the average temp 500 times for plotting

        # reset total temperature
        total_temp = 0

# If total count is not a multiple of 500, calculate the average of the rest data
if count % 500 != 0:
    ave_temp = total_temp / (count % 500)
    ave_temps.extend([ave_temp]*(count % 500)) 

# At the end, plot all the temperatures
times = range(count)
plt.figure(figsize=(12, 6))
plt.plot(times, raw_temps, marker='', linestyle='-', color='b', label = 'Raw Temp')
plt.plot(times, ave_temps, marker='', linestyle='-', color='r', label = 'Ave Temp')
plt.title('Temperature over Time')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (Celsius)')
plt.legend()
plt.savefig('temp_plot.png') # save the plot to a png file

print(count)