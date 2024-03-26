def tricky_timecards(input: str) -> str:
    output = ''
    for line in input.splitlines()[1:]:
        i = 0
        while line[i].isspace():
            i = i + 1
        while line[i].isalnum(): #name
            output += line[i]
            i = i + 1
        output += ' '
        while line[i].isspace():
            i = i + 1
        while line[i].isalnum(): #surname
            output += line[i]
            i = i + 1
        while line[i].isspace():
            i = i + 1
        output += '='
        minutesSum = 0
        timeValues = line.split(',')[1:]
        for timeValue in timeValues:
            timeValueSplitted = timeValue.split(':')
            minutesSum += int(timeValueSplitted[0]) * 60 + int(timeValueSplitted[1])
        hours, minutes = divmod(minutesSum, 60)
        if hours == 1:
            output += '1 hour '
        elif hours > 1:
            output += str(hours) + 'hours '
        if minutes == 1:
            output += '1 minute'
        elif minutes > 1:
            output += str(minutes) + 'minutes'
        output += '\n'
    return output[:-1]

print(tricky_timecards("3\nPeter Gibbons,01:23,04:16,00:59,02:23,00:00\nMilton Waddams,08:00,08:00,08:00,08:00,08:00\nBill Lumbergh,08:31,07:59,06:01,08:55,05:30"))  