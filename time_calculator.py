def add_time(start, duration, day = False):
    # establish days of week in a dict
    days_of_week = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6
    }

    # split the start time and convert str to int
    split_start1 = start.split()
    split_start2 = split_start1[0].split(":")
    ampm = split_start1[1]
    start_hour = int(split_start2[0])
    start_min = int(split_start2[1])

    # split the duration time and convert str to int
    split_dur1 = duration.split()
    split_dur2 = split_dur1[0].split(":")
    dur_hour = int(split_dur2[0])
    dur_min = int(split_dur2[1])

    # convert the start/duration time into minutes
    total_stm = (start_hour * 60) + start_min
    total_dm = (dur_hour * 60) + dur_min
    total_min = total_stm + total_dm
  
    # convert the total minutes into the new time
    total_days = total_min // 60 // 24
    calc_hour = total_min // 60 % 24
    calc_min = total_min % 60

    # establish am/pm and calculate new hours
    if calc_hour > 12 and ampm == "AM":
        new_hour = calc_hour - 12
        ampm = "PM"
    elif calc_hour == 12 and ampm == "AM":
        new_hour = 12
        ampm = "PM"
    elif calc_hour > 12 and ampm == "PM":
        new_hour = calc_hour - 12
        ampm = "AM"
        total_days += 1
    elif calc_hour == 0 and ampm == "AM":
        new_hour = 12
        ampm = "PM"
    elif calc_hour == 0 and ampm == "PM":
        new_hour = 12
        ampm = "AM"
        total_days += 1
    elif calc_hour < 12 and ampm == "AM":
        new_hour = calc_hour
        ampm = "AM"
    elif calc_hour == 12 and ampm == "PM":
        new_hour = 12
        ampm = "AM"
        total_days += 1
    elif calc_hour < 12 and ampm == "PM":
        new_hour = calc_hour
        ampm = "PM"
    
    # calculate new minutes
    if calc_min < 10:
        new_min = "0" + str(calc_min)
    else:
        new_min = calc_min
    
    # format the new time 
    new_time = str(new_hour) + ":" + str(new_min) + " " + ampm
    # establish new day of the week and/or calculate how many days later
    if day == False:
        if total_days == 0:
            return new_time
        elif total_days == 1:
            return new_time + " " + "(next day)"
        else:
            return new_time + " (" + str(total_days) + " " + "days later)"
    else:
        # calculate the day of week if given third arg
        day = day.capitalize()
        calc_day = (days_of_week[day] + total_days) % 7
        for (k, v) in days_of_week.items():
            if calc_day == v:
                new_day = k

        if total_days == 0:
            return new_time + ", " + new_day
        elif total_days == 1:
            return new_time + ", " + new_day + " " + "(next day)"
        else:
            return new_time + ", " + new_day + " (" + str(
                total_days) + " " + "days later)"