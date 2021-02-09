import speedtest
import datetime
import csv

s = speedtest.Speedtest()

with open('test.csv', mode='w', newline='') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv,
                                fieldnames=['time', 'downspeed', 'upspeed'])
    csv_writer.writeheader()
    while True:
        print('iterating')
        time = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        print(downspeed)
        print(upspeed)
        csv_writer.writerow({
            'time': time,
            'downspeed': downspeed,
            "upspeed": upspeed
        })
        speedcsv.flush()
