#!/usr/bin/env python3

import csv
import datetime
import sys

gc_table = []
reader = csv.DictReader(sys.stdin)
for row in reader:
    gcrow = {}
    gcrow['date'] = row['Date']
    game_length = datetime.datetime.strptime(row['End Time'], '%H:%M') \
                  - datetime.datetime.strptime(row['Start Time'], '%H:%M')
    start_time = datetime.datetime.strptime(row['Start Time'], '%H:%M')
    gcrow['time'] = start_time.strftime('%I:%M %p')
    gcrow['duration'] = int(game_length.total_seconds() / 60)
    gcrow['away'] = row['Away Team']
    gcrow['home'] = row['Home Team']
    gcrow['location'] = row['Location'] + ' - ' + row['Field']
    gc_table.append(gcrow)

outfields = ['date', 'time', 'home', 'away', 'location', 'duration']
writer = csv.DictWriter(sys.stdout, fieldnames=outfields)
writer.writeheader()

for row in gc_table:
    writer.writerow(row)
