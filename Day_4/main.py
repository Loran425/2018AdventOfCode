import datetime
import re
from collections import defaultdict


def str2ts(string):
    pattern = '[0-9]+'
    matches = [int(match) for match in re.findall(pattern, string)]
    return datetime.datetime(*matches)


def main():
    ###########################################################################
    # Data Processing
    ###########################################################################

    event_log = []
    with open("./input.txt", mode="r") as input:
        for line in input:
            datestamp, event = line.split(']')
            event_log.append((str2ts(datestamp), event))
    event_log.sort(key=lambda x: x[0])  # Sort by datestamp

    guards = defaultdict(list)
    for event in event_log:
        if re.search('#[0-9]+', event[1]):  # Check for a guard ID ('#' followed by any number of digits)
            guard = int(re.search('[0-9]+', event[1]).group(0))  # Extract the ID
        else:
            guards[guard].append(event[0])

    ###########################################################################
    # Strategy #1
    ###########################################################################
    print("Targeting Using Strategy #1")

    asleep = defaultdict(lambda: 0)
    for guard in sorted(guards):
        events = guards[guard]
        if events:  # Not all guards fall asleep
            for start_time, end_time in zip(events[::2], events[1::2]):
                time_asleep = (end_time - start_time).seconds // 60
                asleep[guard] += time_asleep

    target_guard = sorted(asleep, key=lambda x: asleep[x], reverse=True)[0]
    events = guards[target_guard]

    minutes = [0]*60

    for start_time, end_time in zip(events[::2], events[1::2]):
        for minute in range(start_time.minute, end_time.minute+1):
            minutes[minute] += 1

    target_minute = minutes.index(max(minutes))

    print(f'Target 1: Guard #{target_guard} @ minute {target_minute}, {target_guard*target_minute}\n')

    ###########################################################################
    # Strategy #2
    ###########################################################################
    print("Targeting Using Strategy #2")

    target_asleep = dict()
    for guard in guards:
        minutes = [0]*60
        events = guards[guard]
        for start_time, end_time in zip(events[::2], events[1::2]):
            for minute in range(start_time.minute, end_time.minute + 1):
                minutes[minute] += 1
        target_asleep[guard] = (minutes.index(max(minutes)), max(minutes))

    target = sorted(target_asleep, key=lambda x: target_asleep[x][1], reverse=True)[0]
    print(f'Target 2: Guard #{target} @ minute {target_asleep[target][0]}, {target*target_asleep[target][0]}')


if __name__ == "__main__":
    main()
