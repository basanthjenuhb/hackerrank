time = eval(input())
hr, min, sec, time = int(time[0:2]), int(time[3:5]), int(time[6:8]), time[8:11]
if time == "PM" and hr!=12:hr+=12
elif time == "AM" and hr==12:hr=0
print((str(hr).zfill(2)+":"+str(min).zfill(2)+":"+str(sec).zfill(2)))
